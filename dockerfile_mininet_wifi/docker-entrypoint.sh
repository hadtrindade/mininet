#!/usr/bin/env bash
set -e

echo "Inciando OVS"
service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640

if [ -z $@ ]
then
    bash
else
    python $@ 
fi

echo "Encerrando OVS"
service openvswitch-switch stop
