from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from sys import argv
import os
from time import sleep
spine=int(argv[1])+1
leaf=int(argv[2])+1
os.system('mn -c')
os.system('clear')

class topoSpineLeaf(Topo):
    def __init__( self, spine, leaf ):
        Topo.__init__(self)
        print("subindo topologia")
        for x in range(1,3):
            self.addSwitch('borderl%s'%x, dpid='{:1>16}'.format(x))
        for i in range(1, spine):
            self.addSwitch('spine%s' % i, dpid='{:0>16}'.format(i))
            for j in range(1,leaf):
                if i == 1:
                    self.addSwitch('leaf%s' % j, dpid='{:2>16}'.format(j))
                    self.addHost('h%d' % j)
                    if j == 1:
                        self.addLink('h%d' % j, 'leaf%s' % j, bw=100)
                    self.addLink('h%d' % j, 'leaf%s' % j, bw=100)
                self.addLink('spine%s' % i,'leaf%s' % j, bw=100)
                if j < 3:
                    self.addLink('borderl%s'%j,'spine%s' % i, bw=100)
def init_topo():
    topo=topoSpineLeaf(spine,leaf)
    net = Mininet(topo=topo, controller=RemoteController('c0', ip='127.0.0.1'), link=TCLink)
    net.start()
    print("Esperando a topologia convergir")
    sleep(35)
    print ("Teste de conectividade")
    net.pingAll()
    print ("Gerando trafego nos links")
    hosts = net.hosts
    for s in hosts:
        if s != hosts[0]:
            s.popen('iperf -s -w 20m')
            print("iperf server {}".format(s.IP()))
    for c in hosts:
        if c != hosts[0]:
            hosts[0].popen('iperf -c %s  -t 3600 ' %c.IP())
            sleep(2)
            print("ipert -> {}".format(c.IP()))
    CLI(net)
    net.stop()

if __name__ == '__main__':
    init_topo()
