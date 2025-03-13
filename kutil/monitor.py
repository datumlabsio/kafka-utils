import requests
import argparse
from time import sleep
from datetime import datetime

argparser = argparse.ArgumentParser()
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
    
    while True:
        response = requests.get(f'{CONNECT_URL}/connectors')
        response_json = response.json()
        data = []
        for connector in response_json:
            row = []

            status = get_connection_status(connector)
            state = status['connector']['state']
            tasks = status['tasks']

            row.append(connector)
            row.append(state)
            tasks_status = []
            for t in tasks:
                tasks_status.append(t.get('state'))
            row.append(tasks_status)
            if STATUS_ONLY:
                data.append(row)
            else:
                for t in tasks:
                    row.append(t.get('trace'))
                if state != 'RUNNING' and RESTART_IF_FAILED:
                    row.append('connector not running, will restart')
                    restart_connector(connector)
                data.append(row)
        
        # clear screen
        print_env()
        print('\033c')
        # color header
        print('\033[1;32;40m')
        
        print('--------------------------------------')
        print('Connector Status')
        print('--------------------------------------')

        # color reset
        print('\033[0;37;40m')
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for row in data:
            print(dt)
            print('connect: ', row[0])
            print('status: ', row[1])
            print('tasks: ', row[2])
            if not STATUS_ONLY:
                for r in row[3:]:
                    print(r)
            print('--------------------------------------')
        
        sleep(INTERVAL)
main()