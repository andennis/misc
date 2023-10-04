#!/bin/bash

while [ $# -gt 0 ]; do
  case "$1" in
    --name=*)
      cert_common_name="${1#*=}"
      ;;
    --host=*)
      openvpn_host="${1#*=}"
      ;;
    *)
      printf "Error: Invalid argument: $1\n"
      exit 1
  esac
  shift
done


echo "Generating and signing the client cerificate"
# The CA Key password will be requested
# The result is the following files:
# - /etc/openvpn/easy-rsa/pki/issued/openvpn_client_<cert_common_name>.crt
# - /etc/openvpn/easy-rsa/pki/private/openvpn_client_<cert_common_name>.key
cd /etc/openvpn/easy-rsa
EASYRSA_REQ_CN=$cert_common_name ./easyrsa --batch gen-req openvpn_client_$cert_common_name nopass
./easyrsa --batch sign-req client openvpn_client_$cert_common_name

echo "Client certificate and kay have been created"

# Create OpenVpn configuration file
client_conf_dir="/etc/openvpn/clients"
if [ ! -d $client_conf_dir ]; 
then
    mkdir $client_conf_dir;
    echo "Directory $client_conf_dir has been created"
fi

client_conf="$client_conf_dir/openvpn_client_$cert_common_name.ovpn"

rm -f $client_conf

echo "Generating ovpn file"
cat >$client_conf <<EOF
client
dev tun
proto udp
remote $openvpn_host 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
cipher AES-256-CBC
verb 3
key-direction 1

EOF

ca_key_path=/etc/openvpn/ca.crt
ta_key_path=/etc/openvpn/ta.key
client_crt_path="/etc/openvpn/easy-rsa/pki/issued/openvpn_client_$cert_common_name.crt"
client_key_path="/etc/openvpn/easy-rsa/pki/private/openvpn_client_$cert_common_name.key"

echo "<ca>" >> $client_conf
cat $ca_key_path >> $client_conf
echo "</ca>" >> $client_conf

echo "<cert>" >> $client_conf
cat $client_crt_path >> $client_conf
echo "</cert>" >> $client_conf

echo "<key>" >> $client_conf
cat $client_key_path >> $client_conf
echo "</key>" >> $client_conf
 
echo "<tls-auth>" >> $client_conf
cat $ta_key_path >> $client_conf
echo "</tls-auth>" >> $client_conf

echo "ovpn file has been created: $client_conf"
