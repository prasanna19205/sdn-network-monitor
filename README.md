# SDN Network Utilization Monitor

Monitors bandwidth using Ryu controller and Mininet.

## Setup
```bash
source ~/ryu39-env/bin/activate
ryu-manager monitor.py --ofp-tcp-listen-port 6633
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --switch ovsk,protocols=OpenFlow13
```

## Scenarios
| Test | Result |
|------|--------|
| Ping | 0% loss |
| iperf | 3.4 Gbps |
| Idle | 0.0 bps |

