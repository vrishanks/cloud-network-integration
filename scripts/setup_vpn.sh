#!/bin/bash

VPN_CONFIG_PATH="path/to/your/vpn/config.ovpn"
sudo openvpn --config $VPN_CONFIG_PATH &
