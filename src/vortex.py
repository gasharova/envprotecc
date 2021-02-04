class Vortex:
    def __init__(self):
        self.SECRETS = {}   # Populate with sources
        self.endpoints = set() # Populate with sinks

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

    def register_endpoint(self, func):
        '''
        Registers an endpoint method to track the data flowing through its response.
        Usage example - 
        ```python
        @app.GET
        @vortex.register_endpoint
        def response_function(...):
            ...
        ```
        '''
        def register(*args, **kwargs):
            out = func(*args, **kwargs)
            self.endpoints.add(out)
            return out

        return register
