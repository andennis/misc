# Generate Open VPN client configuration

The script should be located on vpn server in the folder `/etc/openvpn/`

## Usage
```
> /etc/openvpn/openvpn_client_config.sh --name=<config name> --host=<vpn host address>
```

### Example
```
> sudo /etc/openvpn/openvpn_client_config.sh --name=my-pc --host=185.152.139.119
```

### Result
The vpn client configuration file (*.ovpn) will be created in the folder `/etc/openvpn/clients/openvpn_client_<config name>.ovpn`
```
e.g. /etc/openvpn/clients/openvpn_client_my-pc.ovpn
```