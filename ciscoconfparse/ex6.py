"""
This script performs the following actions:
- uses Netmiko to retrieve 'show run' from a device
- feeds this config into CiscoConfParse to find aall of the interfaces that have an IP address
- prints out interface name & ip for each interface that has an IP
"""

from netmiko import ConnectHandler
from getpass import getpass
from ciscoconfparse import CiscoConfParse

device = {
    'host': '<device FQDN>',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_ios',
    'session_log': 'device-running-config.txt'
}

net_connect = ConnectHandler(**device)
net_connect.send_command("show run")

cisco_obj = CiscoConfParse("device-running-config.txt")
match = cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

for obj in range(len(match)):
    interface = match[obj].text
    ip_address = match[obj].children[0].text
    print()
    print("Interface Line:", interface)
    print("IP Address Line:", ip_address)
