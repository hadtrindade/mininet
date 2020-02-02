#!/usr/bin/env bash
set -e

if [ -z $@ ]
then
    bash
else
    ryu-manager $@
fi