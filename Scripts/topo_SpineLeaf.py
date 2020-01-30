from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
import os
from sys import argv

spine=int(argv[1])+1
leaf=int(argv[2])+1

os.system('mn -c')
os.system('clear')

class topoSpineLeaf(Topo):
    def __init__( self, spine, leaf ):
        Topo.__init__(self)
        for x in range(1,3):
            self.addSwitch('borderl%s'%x, dpid='{:1>16}'.format(x))
        for i in range(1, spine):
            self.addSwitch('spine%s' % i, dpid='{:0>16}'.format(i))
            for j in range(1,leaf):
                if i == 1:
                    self.addSwitch('leaf%s' % j, dpid='{:2>16}'.format(j))
                    self.addHost('h%d' % j)
                    self.addLink('h%d' % j, 'leaf%s' % j)
                self.addLink('spine%s' % i,'leaf%s' % j )
                if j < 3:
                    self.addLink('borderl%s'%j,'spine%s' % i)
def init_topo():
    topo=topoSpineLeaf(spine,leaf)
    net = Mininet(topo, controller=RemoteController('c0', ip='127.0.0.1'))
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    init_topo()
