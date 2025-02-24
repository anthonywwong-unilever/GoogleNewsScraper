from typing import List, Optional
from dataclasses import dataclass


@dataclass
class Theme:
    """A theme for sentiment analysis.
    """
    DEMAND: str = 'Demand'
    SUPPLY: str = 'Supply'
    FEEDSTOCK_PRICE: str = 'Feedstock Price'
    COMPONENT_PRICE: str = 'Component Price'


@dataclass
class Article:
    """An article from a news site.
    """
    site: str 
    url: str 
    html_content: str

    def __print__(self) -> None:
        print(f"{self.site}: {self.url}")
        print("\n HTML Content: \n")
        print(self.html_content)


@dataclass
class SearchResult:
    """An article returned by Google search using keyword of a theme.
    """
    keyword: str 
    theme: Theme
    article: Article


@dataclass
class Schema:
    """A schema of info to scrape from news articles.
    """
    TITLE: str = 'title'
    DATE: str = 'date'
    AUTHOR: str = 'author'
    CONTENT: str = 'content'

    def get_columns(self) -> List[str]:
        return list(map(lambda col: col.lower(), self.__annotations__.keys()))
    

@dataclass
class Row:
    """A row of the structured output of news article info.
    """
    site: str
    url: str
    theme: str
    keyword: str 
    title: Optional[str] = None 
    date: Optional[str] = None 
    author: Optional[str] = None 
    content: Optional[str] = None 
    