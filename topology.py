# topology.py
from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def create_network():
    setLogLevel('info')

    net = Mininet(
        controller=RemoteController,
        switch=OVSSwitch,
        autoSetMacs=True
    )

    info('*** Adding controller\n')
    net.addController('c0', controller=RemoteController,
                      ip='127.0.0.1', port=6633)

    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')

    info('*** Adding hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.0.3/24')

    info('*** Adding links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)

    info('*** Starting network\n')
    net.build()
    c0 = net.get('c0')
    s1.start([c0])

    info('*** Setting OpenFlow 1.3\n')
    s1.cmd('ovs-vsctl set bridge s1 protocols=OpenFlow13')

    info('*** Network is UP\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    create_network()

