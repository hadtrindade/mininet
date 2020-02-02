# Mininet

## Docker com mininet
1. [Dockerfile](https://github.com/hadtrindade/mininet/tree/master/docker-mininet)
1. `docker build -t nome:tag .`
1. ### Executar container mininet com bash
1. `docker run -it --rm --name nome_do_container --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /$XAUTHORITY:/root/.Xauthority nome:tag`
1. ### Executar container mininet iniciando topologia, passamdo nome do script e argumentos.
1. `docker run -it --rm --name nome_do_container --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /$XAUTHORITY:/root/.Xauthority -v /scripts:/root  nome:tag nome_script.py arg1 arg2 ...`

## Docker com RYU Controller
1. [Dockerfile](https://github.com/hadtrindade/mininet/tree/master/docker-ryu_controller)
1. `docker build -t nome:tag .`
1. ### Executar container ryu com bash
1. `docker run -it --rm --name ryu nome:tag`
1. ### Executar container ryu iniciando o controller com STP
1. `docker run -it --rm --name ryu nome:tag ryu.app.simple_switch_13`

## Scripts para criação de topologias usando mininet
1. ### Gerando uma topogia com 2 borderleafs, 4 spines e 6 leafs
1. [Scripts](https://github.com/hadtrindade/mininet/tree/master/Scripts)
1. `sudo python topo_SpineLeaf_TC_Iperf.py 4 6`
