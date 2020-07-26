from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])


nxos1 = {
    "device_name": "nxos1",
    "interface": "Ethernet1/1", 
    "ip_address": "10.1.100.1", 
    "netmask": "24",
    "local_as": "22",
    "peer_ip": "10.1.100.2"
}

nxos2 = {
    "device_name": "nxos2",
    "interface": "Ethernet1/1", 
    "ip_address": "10.1.100.2", 
    "netmask": "24",
    "local_as": "22", 
    "peer_ip": "10.1.100.1"
}

for j2_vars in (nxos1, nxos2):
    print()
    print(j2_vars["device_name"])
    print("-----")
    template_file = "ex2b.j2"
    template = env.get_template(template_file)
    output = template.render(**j2_vars)
    print(output)
    print()
