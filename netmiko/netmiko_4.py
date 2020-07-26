"""
Use Netmiko to:
    connect to device using global_delay_factor of 2
    execute 'show lldp neighbors detail'
    print returned output to stdout

Use Python datetime library to record the execution time
"""

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device = {
    'host': '<device FQDN>',
    'username': '<username>',
    'password': getpass(),
    'device_type': 'cisco_nxos',
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
command = 'show lldp neighbors detail'
output = net_connect.send_command(command)
print(output)

datenow = datetime.now()
print(datenow)

