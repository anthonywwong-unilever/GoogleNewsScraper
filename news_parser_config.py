from typing import Dict, List
from scraper.config.metadata import Schema
from scraper.config.news_site import Site, RareSite
from scraper.instructions.infrequent import Instructions


class NewsParserConfig:
    """
    """
    instructions: Dict[str, Dict]
    
    def __init__(self) -> None:
        """
        """
        self.instructions = self._load_parser_instructions()


    def has_instructions(self, site_name: str) -> bool:
        """Check if there is parsing instruction available
        for articles from the news site <site_name>.
        """
        return site_name in self.instructions
    

    def get_instructions(self, site_name: Site) -> Dict[str, str]:
        """Return the parsing instruction for articles from
        the news site <site_name>.
        """
        return self.instructions[site_name]
    

    def instructions_in_scope(self, site_name: Site) -> bool:
        """Check if the set of columns that are instructed to
        be parsed from <site_name>'s articles is within scope.
        """
        columns_in_scope = Schema().get_columns()
        instructions_columns = self.get_instructions(site_name).keys()
        return set(instructions_columns) <= set(columns_in_scope)


    def _load_parser_instructions(self) -> Dict[str, List[Dict]]:
        """Return instructions containing either XPATH or
        CSS selector queries for parsing the HTML text
        of articles from the news source providers. 
        
        The instruction parses, if available, the article's 
        title, date, author, and content, respectively.
        """
        return {
            RareSite.CHEM_ANALYST: Instructions.chem_analyst,
            RareSite.FASTMARKETS: Instructions.fastmarkets,
            RareSite.FAS_USDA: Instructions.fas_usda,
            RareSite.BIODIESEL_MAGAZINE: Instructions.biodiesel_magazine,
            RareSite.BUSINESS_RESEARCH_INSIGHTS: Instructions.business_research_insights,
            RareSite.GLOBE_NEWSWIRE: Instructions.globe_newswire,
            RareSite.THE_EDGE_MALAYSIA: Instructions.the_edge_malaysia,
            RareSite.CLEAN_AIR_TASK_FORCE: Instructions.clean_air_task_force,
            RareSite.THE_LOADSTAR: Instructions.the_loadstar,
            RareSite.TRANSPORT_ENVIRONMENT: Instructions.transport_environment,
            RareSite.GLOBAL_MARKET_INSIGHTS: Instructions.global_market_insights,
            RareSite.GRAND_VIEW_RESEARCH: Instructions.grand_view_research,
            RareSite.RESOURCE_WISE: Instructions.resource_wise,
            RareSite.REUTERS: Instructions.reuters,
            RareSite.RYSTAD_ENERGY: Instructions.rystad_energy,
            RareSite.ERS_USDA: Instructions.ers_usda,
            RareSite.GREEN_CAR_CONGRESS: Instructions.green_car_congress,
            RareSite.WASTE_MANAGEMENT_WORLD: Instructions.waste_management_world,
            RareSite.UNION_OF_CONCERNED_SCIENTISTS: Instructions.union_of_concerned_scientists,
            RareSite.ING_THINK: Instructions.ing_think,
            RareSite.SCIENCE_DIRECT: Instructions.science_direct,
            RareSite.INTERNATIONAL_ENERGY_AGENCY: Instructions.international_energy_agency,
            RareSite.ENERGY_INFORMATION_ADMINISTRATION: Instructions.energy_information_administration,
            RareSite.TRANSPORT_TOPICS: Instructions.transport_topics,
            RareSite.THE_GUARDIAN: Instructions.the_guardian,
            RareSite.NATURE: Instructions.nature,
            RareSite.THE_COUNTER: Instructions.the_counter,
            RareSite.CME_GROUP: Instructions.cme_group,
            RareSite.ET_ENERGYWORLD: Instructions.et_energyworld,
            RareSite.CLARIANT: Instructions.clariant,
            RareSite.BIOFUELS_INTERNATIONAL: Instructions.biofuels_international,
            RareSite.OUR_WORLD_IN_DATA: Instructions.our_world_in_data,
            RareSite.NEW_SCIENTIST: Instructions.new_scientist,
            RareSite.RESEARCH_GATE: Instructions.research_gate,
            RareSite.YAHOO_FINANCE: Instructions.yahoo_finance,
        }
