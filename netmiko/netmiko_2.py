# Use Netmiko to connect to device, retrieve 'show version', & send it to a text file

from netmiko import ConnectHandler
from getpass import getpass


net_connect = ConnectHandler(
    host='device FQDN',
    username='<username>',
    password=getpass(),
    device_type='cisco_ios',
    session_log='<device>_show_version.txt'
)

output = net_connect.send_command("show version")




