import pandas as pd
import logging
import json

class Config:
    with open('config/config.json', 'r') as config_file:
        config = json.load(config_file)

    agent_positions = config['agent_positions']
    lock_in_button_position = config['lock_in_button_position']
    agents_df = pd.DataFrame(agent_positions)
    
    def configure_logging():
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    
