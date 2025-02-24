from scraper.config.metadata import Schema


class Instructions:
    """A list of instructions for for parsing article info from 
    various news provider sites. Each instruction parses the 
    article HTML content using either XPATH or CSS selector. 
    """
    chem_analyst = {
        Schema.TITLE: [
            "article[class='blog-detail-summary'] h1"
        ],
        Schema.DATE: [
            ".//article[@class='blog-detail-summary']/div[@class='relaventnewspublisheddate']//span[*[1][name()='svg']]"
        ],
        Schema.AUTHOR: [
            ".//article[@class='blog-detail-summary']/div[@class='relaventnewspublisheddate']//span[not(*[name()='svg'])]"
        ],
        Schema.CONTENT: [
            [
                "div[class='blog-list-data']"
            ]
        ]
    }

    fastmarkets = {
        Schema.TITLE: [
            "h1[class='Page-headline']"
        ],
        Schema.DATE: [
            "div[class='Page-datePublished']"
        ],
        Schema.AUTHOR: [
            "div[class='Page-authors'] > a"
        ],
        Schema.CONTENT: [
            [
                "div[class='RichTextArticleBody RichTextBody']"
            ]
        ]
    }

    fas_usda = {
        Schema.TITLE: [
            "h1[class='c-page-TITLE__TITLE']"
        ],
        Schema.DATE: [
            "div[class='c-page-TITLE__meta'] > time"
        ],
        Schema.AUTHOR: [
            "span[class='c-contact-inline'] > a:first-child"
        ],
        Schema.CONTENT: [
            [
                ".//div[@class='l-story__body-inner']/hr/preceding-sibling::*"
            ]
        ]
    }

    biodiesel_magazine = {
        Schema.TITLE: [
            "div[class='css-1vkap3'] > div[class='css-1jcc1l1'] > h2[class='chakra-heading css-6jnydr']"
        ],
        Schema.DATE: [
            "p[class='chakra-text css-ah2sm7']"
        ],
        Schema.AUTHOR: [
            "div[class='chakra-stack css-a9v878'] > p[class='chakra-text css-6v0htw']"
        ],
        Schema.CONTENT: [
            [
                "div[class='content css-1ijbxy6']"
            ]
        ]
    }
    
    business_research_insights = {
        
    }

    globe_newswire = {
        
    }

    the_edge_malaysia = {
        
    }

    clean_air_task_force = {
        
    }

    the_loadstar = {
        
    }

    transport_environment = {
        
    }

    global_market_insights = {
        
    }

    grand_view_research = {
        
    }

    resource_wise = {
        
    }

    reuters = {
        
    }

    rystad_energy = {
        
    }

    ers_usda = {
        Schema.TITLE: [
            "div[class='grid-container-desktop-lg'] h1"
        ],
        Schema.DATE: [
            ".//div[@class='grid-container-desktop-lg']/ul/li[contains(@class, 'margin-right-2')]/text()[1]"
        ],
        Schema.AUTHOR: [
            "div[class='grid-container-desktop-lg'] > ul > li[class='tablet:display-inline'] > a"
        ],
        Schema.CONTENT: [
            [
                "div[class='usa-prose']"
            ]
        ]
    }
    
    green_car_congress = {
        
    }

    waste_management_world = {
        
    }

    union_of_concerned_scientists = {
        
    }

    ing_think = {
        
    }

    science_direct = {
        
    }

    international_energy_agency = {
        
    }

    energy_information_administration = {
        Schema.TITLE: [
             "h1 > a"
        ],
        Schema.DATE: [
            "span[class='date']"
        ],
        Schema.AUTHOR: [
            ".//strong[contains(text(), 'contributor')]/parent::p/text()"
        ],
        Schema.CONTENT: [
            [
                ".//div[@class='tie-article']/p[position() < last()]"
            ]
        ]
    }
    
    transport_topics = {
        
    }

    the_guardian = {
        
    }
    
    nature = {
        
    }

    the_counter = {
        
    }

    cme_group = {
        Schema.TITLE: [
            "div[class='article-info'] > h1"
        ],
        Schema.DATE: [
            "span[class='article-date']"
        ],
        Schema.AUTHOR: [
            "div[class='authors']"
        ],
        Schema.CONTENT: [
            [
                "div[class='article-info'] div[class='resource'] div[path='text']",
                ".//main[@id='main-content']/div[last()]/div[1]/div/div/div[2]/*[not(contains(@class, 'component TITLE')) and not(ancestor::*[contains(@class, 'component TITLE')]) and not(contains(@class, 'image')) and not(ancestor::*[contains(@class, 'image')])]"
            ]
        ]
    }

    et_energyworld = {
        
    }

    clariant = {
        
    }
    
    biofuels_international = {
        
    }
    
    our_world_in_data = {
        
    }
    
    new_scientist = {
        
    }
    
    research_gate = {
        
    }
    
    yahoo_finance = {
        
    }








