from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
from getpass import getpass

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])


nxos1 = {
    "device_name": "nxos1",
    "interface": "Ethernet1/2", 
    "ip_address": "10.1.22.1", 
    "netmask": "24",
    "local_as": "22",
    "peer_ip": "10.1.22.2"
}

nxos2 = {
    "device_name": "nxos2",
    "interface": "Ethernet1/2", 
    "ip_address": "10.1.22.2", 
    "netmask": "24",
    "local_as": "22", 
    "peer_ip": "10.1.22.1"
}

nxos1_connect = {
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
}

nxos2_connect = {
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'device_type': 'cisco_nxos',
}


template_file = "ex2b.j2"
template = env.get_template(template_file)
nxos1_output = template.render(**nxos1)
nxos2_output = template.render(**nxos2)
nxos1_cfg = nxos1_output.splitlines()
nxos2_cfg = nxos2_output.splitlines()

from my_devices import nxos1_connect, nxos2_connect 

net_connect = ConnectHandler(**nxos1_connect)
output = net_connect.send_config_set(nxos1_cfg)
print(output)


net_connect = ConnectHandler(**nxos2_connect)
output = net_connect.send_config_set(nxos2_cfg)
print(output)
