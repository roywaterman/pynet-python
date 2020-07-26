from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

template_vars = {
                    "ntp_server1": "130.126.24.24",
                    "ntp_server2": "152.2.21.1",
                    "timezone": "PST",
                    "timezone_offset": "-8 0",
                    "timezone_dst": "PDT"
                }

template_file = "ex5_base.j2"
template = env.get_template(template_file)
output = template.render(**template_vars)
print(output)
