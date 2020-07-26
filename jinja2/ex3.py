from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

my_vars = {"ipv4_enabled": True, "ipv6_enabled": True, "vrf_name": "blue", "rd_number": "100:1"}

template_file = "ex3.j2"
template = env.get_template(template_file)
output = template.render(**my_vars)
print(output)
