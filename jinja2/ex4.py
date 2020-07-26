from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

#vrf_list = {"vrf_name": "blue", "rd_number": "100:1", "ipv4_af": True, "ipv6_af": True}

vrf_entry  = { "vrf1": {"vrf_name": "blue", "rd_number": "100:1", "ipv4_af": True, "ipv6_af": True},
              "vrf2": {"vrf_name": "red", "rd_number": "100:2", "ipv4_af": True},
              "vrf3": {"vrf_name": "white", "rd_number": "100:3", "ipv4_af": True},
              "vrf4": {"vrf_name": "green", "rd_number": "100:4", "ipv4_af": True},
              "vrf5": {"vrf_name": "brown", "rd_number": "100:5", "ipv4_af": True} }
        
template_vars = {"vrf_entry": vrf_entry}

print("test")
template_file = "ex4.j2"
template = env.get_template(template_file)
cfg = template.render(**template_vars)
print(cfg)
print()
