from typing import Dict 


class NewsSiteConfig:
    """
    """
    site_names: Dict[str, str]
    
    def __init__(self) -> None:
        """
        """
        self.site_names = self._load_site_names()


    def get_site_name(self, base_url: str) -> str:
        return self.site_names[base_url]
    

    def _load_site_names(self) -> Dict[str, str]:
        """
        """
        return {
            'www.chemanalyst.com': 'ChemAnalyst',
            'www.fas.usda.gov': 'USDA Foreign Agricultural Service',
            'www.fastmarkets.com': 'Fastmarkets'
        }