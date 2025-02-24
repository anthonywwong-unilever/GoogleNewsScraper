from logging import Logger
from dataclasses import dataclass
from typing import List, Dict, Optional, Union, Generator
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSessionIdException
from scraper.config.metadata import Theme, Article, SearchResult
from scraper.config.news_site_config import SiteConfig
from scraper.utils import setup_logger


@dataclass
class GoogleNewsScraper:
    """A Google News Scraper that searches by keywords and 
    collect news articles.
    """
    _driver: WebDriver
    _logger: Logger
    _search_bar: Optional[WebElement] = None
    _page_wait_time: int = 120
    _element_wait_time: int = 120
    domain: str = "news.google.com"
    site_url: str = "https://news.google.com/home?hl=en-CA&gl=CA&ceid=CA%3Aen"
    _search_bar_css_locator: str = "input[class='Ax4B8 ZAGvjd']"
    _news_css_locator: str = "div[class='UW0SDc']"
    _news_detail_xpath_locator: str = ".//div[@class='IL9Cne']/a[@class='JtKRv']"
    site_config: SiteConfig = SiteConfig()
    
    def __init__(self) -> None:
        self._logger = setup_logger(self.__class__.__name__)
        self._logger.info('Opening Edge browser')
        self._driver = WebDriver()
        self._wait_until(self._page_wait_time)

    def _open_browser(self) -> None:
        try:
            self._driver.current_url
        except InvalidSessionIdException:
            self._logger.info('Opening Edge browser')
            self._driver = WebDriver()
            self._wait_until(self._page_wait_time)

    def _navigate_url(self, site_url: str = None) -> None:
        """Navigate to the URL <site_url> (Google News website by default).
        Wait for the page until it completes loading.
        """
        if site_url is None:
            self._logger.info(f'Navigating to the URL -> {self.site_url}')
            self._driver.get(self.site_url)
            self._wait_until(self._page_wait_time)
        else:
            self._logger.info(f'Navigating to the URL -> {site_url}')
            self._driver.get(site_url)
            self._wait_until(self._page_wait_time)

    def _navigate_article_url(self, article_url: str) -> None:
        """Navigate to the article URL <article_url>. 
        <article_url> is encoded with base64 under Google News domain name. 
        Wait specifically for the URL to change into its actual domain URL.
        """
        self._logger.info(f'Navigating to the Google news article URL -> {article_url}')
        self._driver.get(article_url)
        self._wait_until(self._page_wait_time)

        self._logger.info(f'Waiting for the article URL domain to change from "{self.domain}" to its original domain')
        self._wait_until_url_not_contain(self._element_wait_time, self.domain)

    def _get_search_bar(self) -> None:
        """Get the search bar and save it for input.
        """
        if self._search_bar is None:
            self._wait_until_css_present(self._element_wait_time, self._search_bar_css_locator)

            self._logger.info('Getting the Google News search bar')
            self._search_bar = self._driver.find_element(By.CSS_SELECTOR, self._search_bar_css_locator)

    def _search_keyword(self, keyword: str) -> None:
        """Input search <keyword> and press 'Enter' key.
        """
        if self._search_bar is not None:

            self._logger.info(f'Typing the keyword "{keyword}" in the search bar')
            self._search_bar.send_keys(keyword)  # Input <keyword> into the search bar

            self._logger.info(f'Waiting for the keyword "{keyword}" to show up in the search bar')
            self._wait_until_text_present(self._element_wait_time, self._search_bar_css_locator, keyword)
            self._search_bar.send_keys(Keys.ENTER)  # Press 'Enter' key

            self._logger.info(f'Searching for news articles with keyword {keyword}')
            self._wait_until_css_present(self._element_wait_time, self._news_css_locator)

    def _get_news(self) -> List[WebElement]:
        self._logger.info('Getting the searched articles information')
        self._wait_until_xpath_present(self._element_wait_time, self._news_detail_xpath_locator)
        news = self._driver.find_elements(By.XPATH, self._news_detail_xpath_locator)
        return news
    
    def _get_waitor(self, second: int) -> WebDriverWait:
        return WebDriverWait(self._driver, second)

    def _wait_until(self, second: int) -> None:
        self._logger.info(f'Waiting for page to complete loading (maximum {second} seconds)')
        self._get_waitor(second).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def _wait_until_xpath_present(self, second: int, xpath: str) -> None:
        self._get_waitor(second).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )

    def _wait_until_css_present(self, second: int, css: str) -> None:
        self._get_waitor(second).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, css))
        )

    def _wait_until_text_present(self, second: int, css: str, text: str) -> None:
        self._get_waitor(second).until(
            EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, css), text)
        )

    def _wait_until_url_not_contain(self, second: int, keyword: str) -> None:
        self._get_waitor(second).until(EC.none_of(EC.url_contains(keyword)))

    def finish(self) -> None:
        self._logger.info('Closing the browser')
        self._driver.quit()
    
    def _scrape_article_urls(self, keyword: str, return_dict: bool = False) -> Union[List[str], Dict[str, str]]:
        """Scrape the links of all articles returned by searching for 
        keyword <keyword>. 
        """
        self._open_browser()
        self._navigate_url()
        self._get_search_bar()
        self._search_keyword(keyword)

        self._logger.info(f'Getting the URLs of articles searched using keyword "{keyword}"')

        article_urls = {new.text: new.get_attribute('href') for new in self._get_news() if new.text != ''}

        return article_urls if return_dict else list(article_urls.values())
    
    def _get_article_info(self, article_url: str) -> Article:
        """Get the news site name, original domain's URL, and
        the article's HTML content. 
        """
        self._open_browser()
        self._navigate_article_url(article_url)

        self._logger.info(f'Getting the article\'s site name, domain URL, and HTML content from {article_url}')
        
        site = self.site_config.get_site_name(self._driver.current_url)
        url = self._driver.current_url
        html_content = self._driver.page_source

        return Article(site, url, html_content)
    
    def get_search_articles(self, theme: Theme, keyword: str, urls: List[str] = None) -> Generator[SearchResult]:
        """For each <theme>, scrape the results from articles returned by Google-searching 
        the keyword <keyword>. If a list of article URLs <urls> is provided, then scrape
        those articles only. 
        """
        article_urls = self._scrape_article_urls(keyword) if urls is None else urls
        url_parsed = {article_url: False for article_url in article_urls}     

        try:  
            for article_url in article_urls:
                article = self._get_article_info(article_url) 
                url_parsed[article_url] = True

                self._logger.info(f'Article info successfully scraped from {article_url} \n')
                yield SearchResult(keyword, theme, article)
        except TimeoutError or RuntimeError or ConnectionError:
            self._logger.error('Timeout when parsing an article\'s info. Trying again to parse articles from remaining URLs')
            remaining_urls = [article_url for article_url, parsed in url_parsed.items() if not parsed]
            self.get_search_articles(theme, keyword, remaining_urls)



