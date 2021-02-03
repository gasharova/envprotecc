class Vortex:
    def __init__(self):
        self.SECRETS = {}   # Populate with sources
        self.endpoints = {} # Populate with sinks

    def get_yml(self):
        '''
        Parse .yml/.yaml files and populate SECRETS
        '''
        pass

    def get_env(self):
        '''
        Parse .env files and populate secrets
        '''
        pass

