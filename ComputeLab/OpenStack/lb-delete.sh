#!/bin/bash

for l in $(openstack loadbalancer show $1 -c listeners -f value); do
    pool=$(openstack loadbalancer listener show -c default_pool_id $l -f value)
    for m in $(openstack loadbalancer member list -c id -f value $pool); do
        echo "Deleting member $m from pool $pool"
        openstack loadbalancer member delete $pool $m
    done
    healthmon=$(openstack loadbalancer pool show $pool -c healthmonitor_id -f value)
    if [ -n $healthmon ]; then
        echo "Deleting healthmonitor $healthmon"
        openstack loadbalancer healthmonitor delete $healthmon
    fi
    echo "Deleting pool $pool"
    openstack loadbalancer pool delete $pool
    echo "Deleting listener $l"
    openstack loadbalancer listener delete $l
done
echo "Deleting loadbalancer $1"
openstack loadbalancer delete $1