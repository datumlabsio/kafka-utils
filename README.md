# Kafka Monitoring Utils

available commands:
    kmonitor --help

## Installation

```bash
 python3 -m venv .venv
 source .venv/bin/activate
 pip install git+https://github.com/datumlabsio/kafka-utils
 # (You may ssh port forward) sshpass -p 'xxxx' ssh host -L 8083:localhost:8083
 kmonitor --connect-url http://localhost:8083
```

# Output:
```
--------------------------------------
Connector Status
--------------------------------------
CONNECT_URL http://localhost:8083
STATUS_ONLY False
RESTART_IF_FAILED True
INTERVAL 5

Connector: sink_xxx
State: RUNNING
Tasks: ['RUNNING']
Tasks Trace: []
--------------------------------------
Connector: source_yyy
State: RUNNING
Tasks: ['RUNNING']
Tasks Trace: []
--------------------------------------
Connector: source_zzz
State: RUNNING
Tasks: ['RUNNING']
Tasks Trace: []
--------------------------------------
Connector: sink_hello
State: RUNNING
Tasks: ['RUNNING']
Tasks Trace: []
--------------------------------------
Last Updated: 2025-03-14 02:04:49
```