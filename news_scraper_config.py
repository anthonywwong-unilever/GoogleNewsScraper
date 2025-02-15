from typing import Dict
from scraper.config.metadata import Schema, Quantity, Parser
from selenium.webdriver.common.by import By


class NewsScraperConfig:
    """
    """
    instruction: Dict[str, Dict]
    
    def __init__(self) -> None:
        """
        """
        self.instruction = self.load_scraping_instruction()

    def load_scraping_instruction(self) -> Dict[str, Dict]:
        """
        """
        return {
            "Fastmarkets": {
                Schema.TITLE: {
                    "quantity": Quantity.UNIQUE,
                    "search": {
                        "parser": Parser.SELENIUM,
                        "syntax": By.CSS_SELECTOR,
                        "query": "h1[class='Page-headline']"
                    }
                },
                Schema.SUBTITLE: {
                    "quantity": Quantity.UNIQUE,
                    "search": {
                        "parser": Parser.SELENIUM,
                        "syntax": By.CSS_SELECTOR,
                        "query": "h2[class='Page-subHeadline']"
                    }
                },
                Schema.DATE: {
                    "quantity": Quantity.UNIQUE,
                    "search": {
                        "parser": Parser.SELENIUM,
                        "syntax": By.CSS_SELECTOR,
                        "query": "div[class='Page-datePublished']"
                    }
                },
                Schema.AUTHOR: {
                    "quantity": Quantity.UNIQUE,
                    "search": {
                        "parser": Parser.SELENIUM,
                        "syntax": By.XPATH,
                        "query": ".//div[@class='Page-authors']/a"
                    }
                },
                Schema.TAGS: {
                    "quantity": Quantity.MULTIPLE,
                    "search": {
                        "parser": Parser.SELENIUM,
                        "syntax": By.XPATH,
                        "query": ".//div[@class='Page-tags']/a"
                    }
                },
                Schema.CONTENT: {
                    "quantity": Quantity.MULTIPLE,
                    "search": {
                        "parser": Parser.BS4,
                        "args": {
                            "name": "div",
                            "attrs": {
                                "class": "RichTextArticleBody RichTextBody"
                            }
                        }
                    }
                }
            },
            "ChemAnalyst": {
                Schema.TITLE: {
                    "quantity": Quantity.UNIQUE,
                    "search": {
                        "parser": Parser.SELENIUM,
                        "syntax": By.XPATH,
                        "query": ".//article[@class='blog-detail-summary']/h1"
                    }
                },
                Schema.DATE: {
                    "quantity": Quantity.UNIQUE,
                    "search": {
                        "parser": Parser.SELENIUM,
                        "syntax": By.XPATH,
                        "query": ".//article[@class='blog-detail-summary']/div[@class='relaventnewspublisheddate']//span[*[1][name()='svg']]"
                    }
                },
                Schema.AUTHOR: {
                    "quantity": Quantity.UNIQUE,
                    "search": {
                        "parser": Parser.SELENIUM,
                        "syntax": By.XPATH,
                        "query": ".//article[@class='blog-detail-summary']/div[@class='relaventnewspublisheddate']//span[not(*[name()='svg'])]"
                    }
                },
                Schema.CONTENT: {
                    "quantity": Quantity.MULTIPLE,
                    "search": {
                        "parser": Parser.SELENIUM,
                        "syntax": By.CSS_SELECTOR,
                        "query": "div[class='blog-list-data']"
                    }
                }
            }
            
        }
    
    def has_instruction(self, site_name: str) -> bool:
        """
        """
        return site_name in self.instruction

        