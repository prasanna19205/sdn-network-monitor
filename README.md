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

<img width="802" height="807" alt="cn orange1 " src="https://github.com/user-attachments/assets/62b822b6-ffdb-4e40-a1ca-5caa6b0b9c2a" />
<img width="1290" height="650" alt="cn orange2" src="https://github.com/user-attachments/assets/64686949-6372-44bb-a6fa-07ece9494881" />
<img width="717" height="185" alt="cn orange3" src="https://github.com/user-attachments/assets/e60c6994-d3ca-42ea-80a7-4a9c137c2fa1" />
<img width="1247" height="92" alt="cn orange4" src="https://github.com/user-attachments/assets/cf50762c-c765-44ee-ab49-5305eeb68629" />
<img width="1015" height="302" alt="cn orange5" src="https://github.com/user-attachments/assets/df35b22e-192b-48ec-8ea3-2a32d22a948f" />
<img width="1045" height="365" alt="cn orange6" src="https://github.com/user-attachments/assets/b81e66d8-218f-4f55-9c0e-5389a0d86770" />
<img width="827" height="796" alt="cn orange7" src="https://github.com/user-attachments/assets/ec63de8c-51eb-47e8-8525-de55cf98752e" />
<img width="816" height="795" alt="cn orange8" src="https://github.com/user-attachments/assets/4b134d8c-e3c8-4851-a704-3ca51d0efa1c" />



