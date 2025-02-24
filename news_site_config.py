from typing import Dict, Optional
from scraper.config.news_site import Site, RareSite

import re


class SiteConfig:
    """Config information for various news provider sites. 
    """
    site_names: Dict[str, Site]
    
    def __init__(self) -> None:
        """
        """
        self.site_names = self._load_site_names()


    def get_site_name(self, site_url: str) -> str:
        """Return the site name of the URL <site_url>.
        If the site isn't found in the list of site names, 
        then it is a new site that needs to be included 
        in config. (i.e. 'TBD')
        """
        domain = self._get_site_domain(site_url)
        if domain in self.site_names:
            return self.site_names[domain]
        return 'TBD'
    

    def _get_site_domain(self, site_url: str) -> Optional[str]:
        """Return the domain of <site_url>. (E.g. news.google.com, etc)
        """
        url_pattern = r'http\S*://(\S*?)/\S+'
        base_urls = re.findall(url_pattern, site_url)
        return base_urls[0] if base_urls != [] else None


    def _load_site_names(self) -> Dict[str, Site]:
        """Contains news site base URL and their site names.

        * Needs to be updated to include unseen news site. 

        * Once added a new site (i.e. <base_url>: <site_name>), 
        make sure to update *scraper/config/news_scraper_config.py*
        by doing the following:
        ------------------------------------------------------------
        1. Add <site_name> as a new key in the sraping instruction
        2. Use F12 on web browser to identify relevant CSS/XPath selectors 
           for the information corresponding to the output schema 
        """
        return {
            'www.chemanalyst.com': RareSite.CHEM_ANALYST,
            'www.fastmarkets.com': RareSite.FASTMARKETS,
            'www.fas.usda.gov': RareSite.FAS_USDA,
            'biodieselmagazine.com': RareSite.BIODIESEL_MAGAZINE,
            'www.businessresearchinsights.com': RareSite.BUSINESS_RESEARCH_INSIGHTS,
            'www.globenewswire.com': RareSite.GLOBE_NEWSWIRE,
            'theedgemalaysia.com': RareSite.THE_EDGE_MALAYSIA,
            'www.catf.us': RareSite.CLEAN_AIR_TASK_FORCE,
            'theloadstar.com': RareSite.THE_LOADSTAR,
            'www.transportenvironment.org': RareSite.TRANSPORT_ENVIRONMENT,
            'www.gminsights.com': RareSite.GLOBAL_MARKET_INSIGHTS,
            'www.grandviewresearch.com': RareSite.GRAND_VIEW_RESEARCH,
            'www.resourcewise.com': RareSite.RESOURCE_WISE,
            'www.reuters.com': RareSite.REUTERS,
            'www.rystadenergy.com': RareSite.RYSTAD_ENERGY,
            'www.ers.usda.gov': RareSite.ERS_USDA,
            'www.greencarcongress.com': RareSite.GREEN_CAR_CONGRESS,
            'waste-management-world.com': RareSite.WASTE_MANAGEMENT_WORLD,
            'blog.ucsusa.org': RareSite.UNION_OF_CONCERNED_SCIENTISTS,
            'think.ing.com': RareSite.ING_THINK,
            'www.sciencedirect.com': RareSite.SCIENCE_DIRECT,
            'www.iea.org': RareSite.INTERNATIONAL_ENERGY_AGENCY,
            'www.eia.gov': RareSite.ENERGY_INFORMATION_ADMINISTRATION,
            'www.ttnews.com': RareSite.TRANSPORT_TOPICS,
            'www.theguardian.com': RareSite.THE_GUARDIAN,
            'www.nature.com': RareSite.NATURE,
            'thecounter.org': RareSite.THE_COUNTER,
            'www.cmegroup.com': RareSite.CME_GROUP,
            'energy.economictimes.indiatimes.com': RareSite.ET_ENERGYWORLD,
            'www.clariant.com': RareSite.CLARIANT,
            'biofuels-news.com': RareSite.BIOFUELS_INTERNATIONAL,
            'ourworldindata.org': RareSite.OUR_WORLD_IN_DATA,
            'www.newscientist.com': RareSite.NEW_SCIENTIST,
            'www.researchgate.net': RareSite.RESEARCH_GATE,
            'finance.yahoo.com': RareSite.YAHOO_FINANCE
        }