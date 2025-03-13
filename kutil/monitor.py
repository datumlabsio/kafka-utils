import requests
import argparse
from time import sleep
from datetime import datetime
from .util import ConnectorMonitor, print_env
argparser = argparse.ArgumentParser(
    description='Monitor Kafka Connectors'
)
argparser.add_argument('--connect-url', default='http://localhost:8083')
argparser.add_argument('--status-only', required=False, default=False, action='store_true')
argparser.add_argument('--restart-if-failed', required=False, action='store_true')
argparser.add_argument('--interval', required=False, default=5)
args = argparser.parse_args()

CONNECT_URL = args.connect_url
STATUS_ONLY = args.status_only
RESTART_IF_FAILED = args.restart_if_failed
INTERVAL = int(args.interval)

def main():
    monitor = ConnectorMonitor(CONNECT_URL)
    while True:

        response = requests.get(f'{CONNECT_URL}/connectors')
        response_json = response.json()
        data = []
        for connector in response_json:
            messages = {}
            status = monitor.get_connection_status(connector)
            state = status['connector']['state']
            tasks = status['tasks']

            messages['connector'] = connector
            messages['state'] = state

            tasks_status = []
            tasks_traces = []
            for t in tasks:
                if t.get('state') != 'RUNNING' and RESTART_IF_FAILED:
                    response = monitor.restart_connector(connector)
                    tasks_status.append(t.get('state') + ', Restarting now :' + str(response))
                    tasks_traces.append(t.get('trace'))
                else:
                    tasks_status.append(t.get('state'))

            messages['tasks_trace'] = tasks_traces
            messages['tasks'] = tasks_status
            
            data.append(messages)
    
        print('\033c')
        # color header
        print('\033[1;32;40m')
        
        print('--------------------------------------')
        print('Connector Status')
        print('--------------------------------------')
        print_env(
            CONNECT_URL=CONNECT_URL,
            STATUS_ONLY=STATUS_ONLY,
            RESTART_IF_FAILED=RESTART_IF_FAILED,
            INTERVAL=INTERVAL
        )
        # color reset
        print('\033[0;37;40m')
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for messages in data:
            print(f"Connector: {messages['connector']}")
            print(f"State: {messages['state']}")
            print(f"Tasks: {messages['tasks']}")
            if not STATUS_ONLY:
                print(f"Tasks Trace: {messages['tasks_trace']}")
            print('--------------------------------------')
        print(f"Last Updated: {dt}")
        sleep(INTERVAL)

if __name__ == '__main__':
    main()