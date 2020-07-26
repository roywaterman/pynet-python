"""
Use Netmiko to:
    connect to device
    configure 'ip name-server' and 'ip domain-lookup' commands

Use fast_cli=True to speed up script execution (saves over 5 secs)
"""

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device = {
    'host': '<device FQDN>',
    'username': '<username>',
    'password': getpass(),
    'device_type': 'cisco_ios',
    'fast_cli': True
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

cfg = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']
output = net_connect.send_config_set(cfg)
print(output)

