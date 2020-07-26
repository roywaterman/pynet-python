from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.utils.config import Config
from ex2_jnpr_tables import gather_routes
from pprint import pprint

device = Device(**srx2)
device.open()
device.timeout = 60

print("Routing table before the config change")
print("-" * 40)
routes = gather_routes(device)
pprint(routes.items())

print("Implement config change")
print("-" * 40)
new_static_routes_cfg = Config(device)
new_static_routes_cfg.lock()
new_static_routes_cfg.load(path="ex4.conf", format="text", merge=True)
print(new_static_routes_cfg.diff())
print("Commit the config change")
print("-" * 40)
new_static_routes_cfg.commit()

print("Routing table after the config change")
print("-" * 40)
routes = gather_routes(device)
pprint(routes.items())

print("Backout of config change")
print("-" * 40)
new_static_routes_cfg.load("delete routing-options static route 203.0.113.73/32", format="set", merge=True)
new_static_routes_cfg.load("delete routing-options static route 203.0.113.74/32", format="set", merge=True)
print(new_static_routes_cfg.diff())
new_static_routes_cfg.commit()
new_static_routes_cfg.unlock()

routes = gather_routes(device)
pprint(routes.items())
