from dotenv import find_dotenv, dotenv_values


class Vortex:
    def __init__(self):
        self.SECRETS = {}   # Populate with sources
        self.endpoints = {}  # Populate with sinks

    def get_yml(self):
        '''
        Parse .yml/.yaml files and populate SECRETS
        '''
        pass

    def get_env(self):
        '''
        Parse .env files and populate secrets
        '''
        try:
            dotenv_path = find_dotenv()
            self.SECRETS = dotenv_values(dotenv_path)
        except:
            print(".env file not found in specified location.")


v = Vortex()
v.get_env()

