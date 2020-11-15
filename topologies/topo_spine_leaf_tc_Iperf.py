import argparse
from os import system
from time import sleep
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

parser = argparse.ArgumentParser(
    description="create topology spines and leaves"
    )
parser.add_argument(
    "--spines",
    metavar="spines",
    type=int, nargs="?",
    default="4",
    help="number of spines switchs in topology")
parser.add_argument(
    "--leaves",
    metavar="leaves",
    type=int, nargs="?",
    default="6",
    help="number of leaves switchs in topology")
args = parser.parse_args()

system('mn -c && clear')


class TopoSpineLeaf(Topo):
    def __init__(self, spines, leaves):
        super(TopoSpineLeaf, self).__init__(self)
        for border_leaf in range(1, 3):
            self.addSwitch(
                'borderl%s' % border_leaf,
                dpid='{:1>16}'.format(border_leaf)
                )
        for spine in range(1, spines+1):
            self.addSwitch('spine%s' % spine, dpid='{:0>16}'.format(spine))
            for leaf in range(1, leaves+1):
                if spine == 1:
                    self.addSwitch(
                        'leaf%s' % leaf,
                        dpid='{:2>16}'.format(leaf)
                        )
                    self.addHost('h%d' % leaf)
                    if leaf == 1:
                        self.addLink('h%d' % leaf, 'leaf%s' % leaf, bw=1000)
                    self.addLink('h%d' % leaf, 'leaf%s' % leaf, bw=100)
                self.addLink('spine%s' % spine, 'leaf%s' % leaf, bw=100)
                if leaf < 3:
                    self.addLink('borderl%s' % leaf, 'spine%s' % spine, bw=100)


def start_topology():
    topo = TopoSpineLeaf(args.spines, args.leaves)
    net = Mininet(topo, controller=RemoteController(
        'c0', ip='127.0.0.1'),
        link=TCLink
        )
    net.start()
    net.pingAll()
    hosts = net.hosts
    for s in hosts:
        if s != hosts[0]:
            s.popen('iperf -s -u -w 20m')
            print("iperf server {}".format(s.IP()))
    for c in hosts:
        if c != hosts[0]:
            hosts[0].popen('iperf -c %s -u -b 100m -t 3600 ' % c.IP())
            sleep(2)
            print("ipert -> {}".format(c.IP()))
    CLI(net)
    net.stop()


if __name__ == '__main__':
    start_topology()