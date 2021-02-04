from dotenv import find_dotenv, dotenv_values
import yaml


class Vortex:
    def __init__(self):
        self.SECRETS = {}   # Populate with sources
        self.endpoints = {}  # Populate with sinks

    def get_yml(self, yml_path):
        '''
        Parse .yml/.yaml files and populate SECRETS
        '''
        try:
            with open(yml_path) as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                self.SECRETS.update(data)
        except:
            print(".yml or .yaml file not found in specified location.")

    def get_env(self):
        '''
        Parse .env files and populate secrets
        '''
        try:
            dotenv_path = find_dotenv()
            self.SECRETS.update(dotenv_values(dotenv_path))
        except:
            print(".env file not found in specified location.")

