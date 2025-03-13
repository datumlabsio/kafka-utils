
from logging import getLogger
import requests

logger = getLogger(__name__)
logger.setLevel('INFO')
class ConnectorMonitor:
    def __init__(self, connect_url):
        self.connect_url = connect_url
    
    def get_connection_status(self, connector_name):
        response = requests.get(f'{self.connect_url}/connectors/{connector_name}/status')
        response_json = response.json()
        return response_json

    def restart_connector(self, connector_name):
        response = requests.post(f'{{self.connect_url}}/connectors/{connector_name}/restart?includeTasks=true&onlyFailed=True')
        return response

def print_env(*args, **kwargs):
    """
    Print variables in key value format
    """
    for key, value in kwargs.items():
        print(key, value)

