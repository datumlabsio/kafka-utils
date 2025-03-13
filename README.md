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
