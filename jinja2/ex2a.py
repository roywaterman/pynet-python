from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])


nxos1 = {"interface": "Ethernet1/1", "ip_address": "10.1.100.1", "netmask": "24"}
nxos2 = {"interface": "Ethernet1/1", "ip_address": "10.1.100.2", "netmask": "24"}
nxos1_bgp = {"local_as": "22", "peer_ip": "10.1.100.2"}
nxos2_bgp = {"local_as": "22", "peer_ip": "10.1.100.1"}

print(nxos1)
template_file = "ex2a.j2"
template = env.get_template(template_file)
output = template.render(**nxos1)
print(output)
template_file = "ex2a-bgp.j2"
template = env.get_template(template_file)
output = template.render(**nxos1_bgp)
print(output)

print("nxos2")
template_file = "ex2a.j2"
template = env.get_template(template_file)
output = template.render(**nxos2)
print(output)
template_file = "ex2a-bgp.j2"
template = env.get_template(template_file)
output = template.render(**nxos2_bgp)
print(output)

