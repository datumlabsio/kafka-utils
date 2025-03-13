
from logging import getLogger
import requests

logger = getLogger(__name__)

def get_connection_status(connector_name):
    response = requests.get(f'{CONNECT_URL}/connectors/{connector_name}/status')
    response_json = response.json()
    return response_json

def restart_connector(connector_name):
    response = requests.post(f'{CONNECT_URL}/connectors/{connector_name}/restart?includeTasks=true&onlyFailed=True')
    return response

def print_env(*args, **kwargs):
    """
    Print variables in key value format
    """
    for key, value in kwargs.items():
        print(key, value)
    # for 

    # print('CONNECT_URL:', CONNECT_URL)
    # print('STATUS_ONLY:', STATUS_ONLY)
    # print('RESTART_IF_FAILED:', RESTART_IF_FAILED)
