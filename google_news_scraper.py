from typing import List, Any, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from scraper.config.metadata import Theme, Article 


class GoogleNewsScraper:
    """
    """
    site_url: str
    _driver: webdriver
    _search_bar: Optional[Any]

    def __init__(self) -> None:
        self._driver = webdriver.Edge()
        self.site_url = "https://news.google.com/home?hl=en-CA&gl=CA&ceid=CA%3Aen"

    def _get_site_url(self, site: str = None) -> None:
        if site is None:
            self._driver.get(self.site_url)
        else:
            self._driver.get(site)

    def _get_search_bar(self) -> None:
        self._search_bar = self._driver.find_element(By.CSS_SELECTOR, "input[class='Ax4B8 ZAGvjd']")
    
    def _enter_keyword(self, keyword: str) -> None:
        self._search_bar.send_keys(keyword)

    def _search_keyword(self) -> None:
        self._search_bar.send_keys(Keys.ENTER)

    def _find_news(self) -> List[Any]:
        return self._driver.find_elements(By.XPATH, ".//div[@class='IL9Cne']/a[@class='JtKRv']")
    
    def _get_news_site(self) -> List[Any]:
        return self._driver.find_elements(By.CSS_SELECTOR, "div[class='vr1PYe']")
    
    def _exit_browser(self) -> None:
        self._driver.quit()
    
    def get_articles(self, theme: str, keyword: str) -> List[Article]:

        self._get_site_url()
        # wait 
        self._get_search_bar()
        # wait
        self._enter_keyword(keyword)
        # wait
        self._search_keyword()
        # wait
        news = self._find_news()
        # wait
        articles = []
        for new in news:
            article_title = new.text
            article_link = new.get_attribute('href')

            self._get_site(article_link)
            # wait

            article_html = self._driver.page_source
            article_html_text = BeautifulSoup(article_html, 'html.parser')

            Article()



        