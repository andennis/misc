#!/bin/bash

# registry service domain name
REGISTRY_NAME="registry.local"
# registry service IP
REGISTRY_IP=$1

if [ -z "$REGISTRY_IP" ]
then
   echo "ERROR: Registry service IP address is required";
   exit 1
fi

echo "Adding registry domain entry \"$REGISTRY_IP $REGISTRY_NAME\" to all the worker nodes"

for host_ip in $(kubectl get nodes -o go-template-file=worker_nodes.gotmpl);
do
    echo "Adding entry to the host $host_ip"
    ssh -i ~/.ssh/prod-k8s-room-key.pem ubuntu@$host_ip \
      "grep -q \"$REGISTRY_IP\|$REGISTRY_NAME\" /etc/hosts && echo \"$REGISTRY_NAME entry already exists on $host_ip\" || echo \"$REGISTRY_IP $REGISTRY_NAME\" | sudo tee -a /etc/hosts";
done
