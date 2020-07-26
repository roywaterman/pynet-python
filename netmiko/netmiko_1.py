# Use Netmiko to connect to device & print device prompt

from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    host = '<device FQDN>',
    username = '<username>',
    password = getpass(),
    device_type = 'cisco_ios',
)

print(net_connect.find_prompt())

