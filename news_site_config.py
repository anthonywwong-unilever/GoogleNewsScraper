from typing import Dict, Optional
from scraper.config.news_site import Site

import re


class SiteConfig:
    """Config information for various news provider sites. 
    """
    site_names: Dict[str, str]
    
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


    def _load_site_names(self) -> Dict[str, str]:
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
            'www.chemanalyst.com': Site.CHEM_ANALYST,
            'www.fastmarkets.com': Site.FASTMARKETS,
            'www.fas.usda.gov': Site.FAS_USDA,
            'biodieselmagazine.com': Site.BIODIESEL_MAGAZINE,
            'www.businessresearchinsights.com': Site.BUSINESS_RESEARCH_INSIGHTS,
            'www.globenewswire.com': Site.GLOBE_NEWSWIRE,
            'theedgemalaysia.com': Site.THE_EDGE_MALAYSIA,
            'www.catf.us': Site.CLEAN_AIR_TASK_FORCE,
            'theloadstar.com': Site.THE_LOADSTAR,
            'www.transportenvironment.org': Site.TRANSPORT_ENVIRONMENT,
            'www.gminsights.com': Site.GLOBAL_MARKET_INSIGHTS,
            'www.grandviewresearch.com': Site.GRAND_VIEW_RESEARCH,
            'www.resourcewise.com': Site.RESOURCE_WISE,
            'www.reuters.com': Site.REUTERS,
            'www.rystadenergy.com': Site.RYSTAD_ENERGY,
            'www.ers.usda.gov': Site.ERS_USDA,
            'www.greencarcongress.com': Site.GREEN_CAR_CONGRESS,
            'waste-management-world.com': Site.WASTE_MANAGEMENT_WORLD,
            'blog.ucsusa.org': Site.UNION_OF_CONCERNED_SCIENTISTS,
            'think.ing.com': Site.ING_THINK,
            'www.sciencedirect.com': Site.SCIENCE_DIRECT,
            'www.iea.org': Site.INTERNATIONAL_ENERGY_AGENCY,
            'www.eia.gov': Site.ENERGY_INFORMATION_ADMINISTRATION,
            'www.ttnews.com': Site.TRANSPORT_TOPICS,
            'www.theguardian.com': Site.THE_GUARDIAN,
            'www.nature.com': Site.NATURE,
            'thecounter.org': Site.THE_COUNTER,
            'www.cmegroup.com': Site.CME_GROUP,
            'energy.economictimes.indiatimes.com': Site.ET_ENERGYWORLD,
            'www.clariant.com': Site.CLARIANT,
            'biofuels-news.com': Site.BIOFUELS_INTERNATIONAL,
            'ourworldindata.org': Site.OUR_WORLD_IN_DATA,
            'www.newscientist.com': Site.NEW_SCIENTIST,
            'www.researchgate.net': Site.RESEARCH_GATE,
            'finance.yahoo.com': Site.YAHOO_FINANCE
        }