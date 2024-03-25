import pandas as pd
import logging
import json

class Config:
    with open('config/config.json', 'r') as config_file:
        config = json.load(config_file)

    agent_positions = config['agent_positions']
    lock_in_button_position = config['lock_in_button_position']
    agents_df = pd.DataFrame(agent_positions)
    opened_the_program_count = config['opened_the_program_count']
    
    def configure_logging():
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    
    def increment_opened_the_program_count():
        Config.opened_the_program_count += 1
        with open('config/config.json', 'w') as config_file:
            Config.config['opened_the_program_count'] = Config.opened_the_program_count
            json.dump(Config.config, config_file, indent=4)

    def read_version_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()  # Read the version and strip any whitespace
        except FileNotFoundError:
            return "unknown"  # If the file does not exist, return 'unknown'