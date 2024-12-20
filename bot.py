import json
from handlers.rollbit_handler import rollbit_handler

def main():
    # Load the configuration
    with open("config.json", "r") as f:
        config = json.load(f)

    # Handle Rollbit platform
    rollbit_config = config["platforms"]["rollbit"]
    print("=== Starting Rollbit Trading Bot ===")
    rollbit_handler(rollbit_config)

if __name__ == "__main__":
    main()
