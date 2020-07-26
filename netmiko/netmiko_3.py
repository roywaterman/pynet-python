# Use Netmiko to connect to device & run an extended ping

from netmiko import ConnectHandler
from getpass import getpass

device = {
    'host': '<device FQDN>',
    'username': '<username>',
    'password': getpass(),
    'device_type': 'cisco_ios',
}

net_connect = ConnectHandler(**device)
# I put end = '' in order to get device prompt on same line as ping
print(net_connect.find_prompt(), end='')
# I used '\n' below with strip_command=False in order to send a new line & show it
# This results in a new line each time
command = 'ping'
output = net_connect.send_command_timing(command, strip_command=False)
output += net_connect.send_command_timing('\n', strip_command=False)
output += net_connect.send_command_timing('8.8.8.8', strip_command=False)
output += net_connect.send_command_timing('\n', strip_command=False)
output += net_connect.send_command_timing('\n', strip_command=False)
output += net_connect.send_command_timing('\n', strip_command=False)
output += net_connect.send_command_timing('\n', strip_command=False)
output += net_connect.send_command_timing('\n', strip_command=False)
print(output)

