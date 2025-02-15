from typing import Dict, List, Literal
from dataclasses import dataclass


@dataclass
class Quantity:
    """
    """
    UNIQUE: str = 'unique'
    MULTIPLE: str = 'multiple'  


@dataclass
class Theme:
    """A theme for sentiment analysis.
    """
    DEMAND: str = 'demand'
    SUPPLY: str = 'supply'
    FEEDSTOCK_PRICE: str = 'feedstock price'
    COMPONENT_PRICE: str = 'component price'


@dataclass
class Article:
    """An article from a news site.
    """
    site: str
    link: str 
    theme: Theme
    keyword: str
    html_text: str


@dataclass
class Parser:
    """An HTML parser to extract news text.
    """
    SELENIUM: str = 'selenium'
    BS4: str = 'beautiful soup'


@dataclass
class Schema:
    """The output schema of scraped news articles.
    """
    TITLE: str = 'title'
    SUBTITLE: str = 'subtitle'
    DATE: str = 'date'
    AUTHOR: str = 'author'
    TAGS: str = 'tags'
    SITE: str = 'site'
    LINK: str = 'link'
    THEME: str = 'theme'
    KEYWORD: str = 'keyword'
    CONTENT: str = 'contents'

    def get_pd_schema() -> Dict[str, str]:
        return {
            'title': 'string',
            'subtitle': 'string',
            'date': 'dbdate',
            'author': 'string',
            'tags': 'string',
            'site': 'string',
            'link': 'string',
            'theme': 'string',
            'keyword': 'string',
            'content': 'string'
        }
    
    






