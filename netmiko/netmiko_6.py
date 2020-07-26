"""
Use Netmiko to:
    connect to 2 devices
    configure vlans on both devices (vlan config stored in separate text file)

Use send_config_from_file() method to accomplish this
VLAN config file contents:
--------
vlan 151
 name vlan_151
vlan 152
 name vlan_152
end
--------
"""

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device1 = {
    'host': '<device1 FQDN>',
    'username': '<username>',
    'password': getpass(),
    'device_type': 'cisco_nxos',
}

device2 = {
    'host': '<device2 FQDN>',
    'username': '<username>',
    'password': getpass(),
    'device_type': 'cisco_nxos'
}

switch_list = [device1, device2]
for switch in switch_list:
    net_connect = ConnectHandler(**switch) # perform net_connect for device1, then device2
    print(net_connect.find_prompt())
    output = net_connect.send_config_from_file(config_file='vlan_config.txt')
    print(output)
    save_out = net_connect.save_config() # save the vlan config change
    print(save_out) # print out the saving of the config change





net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

cfg = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']
output = net_connect.send_config_set(cfg)
print(output)

