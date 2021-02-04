from dotenv import find_dotenv
import os


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
            dotenv_file = open(dotenv_path, 'r')
            contents = dotenv_file.readlines()
            for line in contents:
                variable = line.split("=")
                key = variable[0]
                value = variable[1]
                if value == 'true':
                    value = True
                elif value == 'false':
                    value = False
                else:  # TODO: Define other types parsing OR use default load_dotenv
                    value = value.replace('\n', '')
                    value = value.replace('"', '')
                self.SECRETS[key] = value
                print(self.SECRETS)
        except:
            print(".env file not found in specified location.")


v = Vortex()
v.get_env()

