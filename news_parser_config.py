from typing import Dict
from scraper.config.metadata import Schema
from scraper.config.news_site import Site


class NewsParserConfig:
    """
    """
    instruction: Dict[str, Dict]
    
    def __init__(self) -> None:
        """
        """
        self.instruction = self.load_parser_instruction()


    def has_instruction(self, site_name: str) -> bool:
        """Check if there is parsing instruction available
        for articles from the news site <site_name>.
        """
        return site_name in self.instruction
    

    def get_instruction(self, site_name: Site) -> Dict[str, str]:
        """Return the parsing instruction for articles from
        the news site <site_name>.
        """
        return self.instruction[site_name]
    

    def instruction_in_scope(self, site_name: Site) -> bool:
        """Check if the set of columns that are instructed to
        be parsed from <site_name>'s articles is within scope.
        """
        columns_in_scope = Schema().get_columns()
        instruction_columns = self.get_instruction(site_name).keys()
        return set(instruction_columns) <= set(columns_in_scope)


    def load_parser_instruction(self) -> Dict[str, Dict]:
        """Return instructions containing either XPATH or
        CSS selector queries for parsing the HTML text
        of articles from the news source providers. 
        
        The instruction parses, if available, the article's 
        title, date, author, and content, respectively.

        --------------------------------------------------
        |      Definition - (Minimal Content Tag)        |
        --------------------------------------------------
        An HTML tag, <t1>, is called a minimal content tag
        if there's any tag, <t2>, that contains the full content 
        of the article, then <t1> is either <t2> or <t1> is a 
        child of <t2>.

        * The query of article content should find the 
        minimal content tag. 
        """
        return {
            Site.CHEM_ANALYST: {
                Schema.TITLE: "article[class='blog-detail-summary'] h1",
                Schema.DATE: ".//article[@class='blog-detail-summary']/div[@class='relaventnewspublisheddate']//span[*[1][name()='svg']]",
                Schema.AUTHOR: ".//article[@class='blog-detail-summary']/div[@class='relaventnewspublisheddate']//span[not(*[name()='svg'])]",
                Schema.CONTENT: "div[class='blog-list-data']"
            },
            Site.FASTMARKETS: {
                Schema.TITLE: "h1[class='Page-headline']",
                Schema.DATE: "div[class='Page-datePublished']",
                Schema.AUTHOR: "div[class='Page-authors'] > a",
                Schema.CONTENT: "div[class='RichTextArticleBody RichTextBody']"
            },
            Site.FAS_USDA: {
                Schema.TITLE: "h1[class='c-page-title__title']",
                Schema.DATE: "div[class='c-page-title__meta'] > time",
                Schema.AUTHOR: "span[class='c-contact-inline'] > a:first-child",
                Schema.CONTENT: ".//div[@class='l-story__body-inner']/hr/preceding-sibling::*"
            },
            Site.BIODIESEL_MAGAZINE: {
                Schema.TITLE: "div[class='css-1vkap3'] > div[class='css-1jcc1l1'] > h2[class='chakra-heading css-6jnydr']",
                Schema.DATE: "p[class='chakra-text css-ah2sm7']",
                Schema.AUTHOR: "div[class='chakra-stack css-a9v878'] > p[class='chakra-text css-6v0htw']",
                Schema.CONTENT: "div[class='content css-1ijbxy6']"
            },
            Site.BUSINESS_RESEARCH_INSIGHTS: {},
            Site.GLOBE_NEWSWIRE: {},
            Site.THE_EDGE_MALAYSIA: {},
            Site.CLEAN_AIR_TASK_FORCE: {},
            Site.THE_LOADSTAR: {},
            Site.TRANSPORT_ENVIRONMENT: {},
            Site.GLOBAL_MARKET_INSIGHTS: {},
            Site.GRAND_VIEW_RESEARCH: {},
            Site.RESOURCE_WISE: {},
            Site.REUTERS: {},
            Site.RYSTAD_ENERGY: {},
            Site.ERS_USDA: {
                Schema.TITLE: "div[class='grid-container-desktop-lg'] h1",
                Schema.DATE: ".//div[@class='grid-container-desktop-lg']/ul/li[contains(@class, 'margin-right-2')]/text()[1]",
                Schema.AUTHOR: "div[class='grid-container-desktop-lg'] > ul > li[class='tablet:display-inline'] > a",
                Schema.CONTENT: "div[class='usa-prose']"
            },
            Site.GREEN_CAR_CONGRESS: {},
            Site.WASTE_MANAGEMENT_WORLD: {},
            Site.UNION_OF_CONCERNED_SCIENTISTS: {},
            Site.ING_THINK: {},
            Site.SCIENCE_DIRECT: {},
            Site.INTERNATIONAL_ENERGY_AGENCY: {},
            Site.ENERGY_INFORMATION_ADMINISTRATION: {
                Schema.TITLE: "h1 > a",
                Schema.DATE: "span[class='date']",
                Schema.AUTHOR: ".//strong[contains(text(), 'contributor')]/parent::p/text()",
                Schema.CONTENT: ".//div[@class='tie-article']/p[position() < last()]"
            },
            Site.TRANSPORT_TOPICS: {},
            Site.THE_GUARDIAN: {},
            Site.NATURE: {},
            Site.THE_COUNTER: {},
            Site.CME_GROUP: {
                Schema.TITLE: "div[class='article-info'] > h1",
                Schema.DATE: "span[class='article-date']",
                Schema.AUTHOR: "div[class='authors']",
                Schema.CONTENT: [
                    "div[class='article-info'] div[class='resource'] div[path='text']",
                    ".//main[@id='main-content']/div[last()]/div[1]/div/div/div[2]/*[not(contains(@class, 'component title')) and not(ancestor::*[contains(@class, 'component title')]) and not(contains(@class, 'image')) and not(ancestor::*[contains(@class, 'image')])]"
                ]
            },
            Site.ET_ENERGYWORLD: {},
            Site.CLARIANT: {},
            Site.BIOFUELS_INTERNATIONAL: {},
            Site.OUR_WORLD_IN_DATA: {},
            Site.NEW_SCIENTIST: {},
            Site.RESEARCH_GATE: {},
            Site.YAHOO_FINANCE: {}
        }
