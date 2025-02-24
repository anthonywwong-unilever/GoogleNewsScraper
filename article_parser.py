from typing import List, Optional
from functools import reduce
from dataclasses import dataclass
from parsel import Selector
from scraper.utils import Logger, setup_logger 
from scraper.config.news_parser_config import NewsParserConfig
from scraper.config.metadata import Row, Schema, SearchResult

import numpy as np
import pandas as pd


@dataclass
class ArticleParser:
    """
    """
    search_results: List[SearchResult]
    _logger: Logger
    config: NewsParserConfig = NewsParserConfig()

    def __init__(self, search_results: List[SearchResult]) -> None:
        self.search_results = search_results
        self._logger = setup_logger(self.__class__.__name__)

    def _piecewise_parse(self, query: str, selector: Selector) -> List[str]:
        """
        """
        if '/' in query and 'text()' in query:
            return selector.xpath(query).getall()
        elif '/' in query:
            return selector.xpath(query).css('*::text').getall()
        elif '::text' in query:
            return selector.css(query).getall()
        else:
            return selector.css(f'{query} *::text').getall()
        
    def _parse(self, queries: List[str], selector: Selector) -> List[str]: 
        """
        """
        piecewise_values = [self._piecewise_parse(query, selector) for query in queries]
        return reduce(lambda x, y: x + y, piecewise_values)
    
    def _try_value(self, possible_query: str, selector: Selector) -> Optional[str]:
        """
        """
        column_value = self._piecewise_parse(possible_query, selector)
        return column_value[0].strip() if column_value != [] else None

    
    def _try_join_values(self, queries: List[str], selector: Selector) -> Optional[str]:
        """
        """
        column_values = self._parse(queries, selector)
        return '\n'.join([text.strip() for text in column_values]).strip() if column_values != [] else None
        

    def get_value(self, column: str, possible_queries: List[str], selector: Selector, site: str) -> Optional[str]:
        """
        """
        possible_values = map(lambda possible_query: self._try_value(possible_query, selector), possible_queries)
        not_null_values = list(filter(lambda possible_value: possible_value is not None, possible_values))

        if not_null_values != []:
            self._logger.info(f'Successfully parsed the article\'s {column} info')
            return not_null_values[0].strip()  
        else:
            self._logger.error(f'No info parsed for article\'s {column}. Either no info present or need to add a new instruction under "{site}"')
            return None
        
    
    def get_join_values(self, column: str, possible_queries_list: List[List[str]], selector: Selector, site: str) -> Optional[str]:
        """
        """
        possible_values = map(lambda possible_queries: self._try_join_values(possible_queries, selector), possible_queries_list)
        not_null_values = list(filter(lambda possible_value: possible_value is not None, possible_values))

        if not_null_values != []:
            self._logger.info(f'Successfully parsed the article\'s {column} info')
            return not_null_values[0].strip()  
        else:
            self._logger.error(f'No info parsed for article\'s {column}. Either no info present or need to add a new instruction under "{site}"')
            return None


    def parse_articles(self) -> List[Row]:
        """
        """

        rows = []
        for search_result in self.search_results:

            column_values = {
                'site': search_result.article.site,
                'url': search_result.article.url,
                'theme': search_result.theme,
                'keyword': search_result.keyword
            }

            self._logger.info(f'Begin parsing the article -> "{search_result.article.site}": {search_result.article.url}')
            try:
                self._logger.info(f'Checking if there\'s instructions available for parsing articles from "{search_result.article.site}"')
                instructions = self.config.get_instructions(search_result.article.site)
                self._logger.info(f'Instruction available for "{search_result.article.site}"')

                self._logger.info(f'Checking if the instruction for parsing articles from "{search_result.article.site}" is in scope')
                if not self.config.instructions_in_scope(search_result.article.site):
                    self._logger.error(f'Instructions out of scope! Need to update the parser config for "{search_result.article.site}"')
                    raise AttributeError
                self._logger.info(f'Instruction in scope for "{search_result.article.site}"')

                if Schema.TITLE not in instructions:
                    column_values[Schema.TITLE] = None
                if Schema.DATE not in instructions:
                    column_values[Schema.DATE] = None 
                if Schema.AUTHOR not in instructions:
                    column_values[Schema.AUTHOR] = None 
                if Schema.CONTENT not in instructions:
                    column_values[Schema.CONTENT] = None

                selector = Selector(text=search_result.article.html_content)

                for column, possible_queries in instructions.items():
                    if isinstance(possible_queries[0], str):
                        syntax = list(set(map(lambda q: 'XPATH' if '/' in q else 'CSS', possible_queries)))
                        self._logger.info(f'Parsing the article\'s {column} using {syntax[0] if len(syntax) == 1 else 'CSS and XPATH'}')
                        column_values[column] = self.get_value(column, possible_queries, selector, search_result.article.site)
                    else:
                        # syntax = list(set(map(lambda queries: , possible_queries)))
                        column_values[column] = self.get_join_values(column, possible_queries, selector, search_result.article.site)  

                # for column, query in instructions.items():
                #     if isinstance(query, str):
                #         self._logger.info(f'Parsing the article\'s {column} using {'XPATH' if '/' in query else 'CSS'}')    
                #         column_values[column] = self.get_value(column, query, selector, search_result.article.site)
                #     else:
                #         sytax = list(set(map(lambda q: 'XPATH' if '/' in q else 'CSS', query)))
                #         self._logger.info(f'Parsing the article\'s {column} using {sytax[0] if len(sytax) == 1 else 'CSS and XPATH'}')
                #         column_values[column] = self.get_join_values(column, query, selector, search_result.article.site)

                self._logger.info(f'Finish parsing the article -> "{search_result.article.site}": {search_result.article.url} \n')
                rows.append(Row(**column_values))

            except KeyError or AttributeError:  # Cannot find the news site in parser config
                
                self._logger.error(f'Unable to parse the article! Need to update either the site config or parsing instruction -> "{search_result.article.site}": {search_result.article.url} ')
                for schema_col in Schema().get_columns():
                    column_values[schema_col] = None

                rows.append(Row(**column_values))

        return rows
    
    def tabulate_articles(self) -> pd.DataFrame:
        """
        """
        article_rows = self.parse_articles()
        return pd.DataFrame({
            'site': [row.site for row in article_rows],
            'url': [row.url for row in article_rows],
            'theme': [row.theme for row in article_rows],
            'keyword': [row.keyword for row in article_rows],
            'title': [row.title if row.title is not None else np.nan for row in article_rows],
            'date': [row.date if row.date is not None else np.nan for row in article_rows],
            'author': [row.author if row.author is not None else np.nan for row in article_rows],
            'content': [row.content if row.content is not None else np.nan for row in article_rows]
        }).astype({
            'site': 'string',
            'url': 'string',
            'theme': 'string',
            'keyword': 'string',
            'title': 'string',
            'date': 'string',
            'author': 'string',
            'content': 'string'
        })
