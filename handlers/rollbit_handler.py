from handlers.api_handler.py import rollbit_api_handler
from handlers.scraper_handler import rollbit_scraper_handler

def rollbit_handler(config):
    mode = config["mode"]
    pairs = config["pairs"]
    
    if mode == "api":
        api_key = config["api_key"]
        api_secret = config["api_secret"]
        rollbit_api_handler(api_key, api_secret, pairs)
    elif mode == "scraper":
        rollbit_scraper_handler(config["url"], pairs)
    else:
        raise ValueError("Invalid mode! Choose 'api' or 'scraper'.")
