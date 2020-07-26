import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")
interface_data = output['TABLE_interface']['ROW_interface']
print("Interface: {interface}; State: {state}; MTU: {eth_mtu}".format(**interface_data)) 
print(f"Interface: {interface_data['interface']}; State: {interface_data['state']}; MTU: {interface_data['eth_mtu']}")

