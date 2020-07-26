import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from nxapi_plumbing import Device
from getpass import getpass

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

## Exercise 7a ##
xml_object = device.show("show interface Ethernet1/1")
#etree.tostring(xml_object).decode()
interface = xml_object.find(".//interface").text
state = xml_object.find(".//state").text
mtu = xml_object.find(".//eth_mtu").text
print(f"Interface: {interface}; State: {state}; MTU: {mtu}")

## Exercise 7b ##
cmds = ["show system uptime", "show system resources"]
output = device.show_list(cmds)
for cmd in output:
    print(etree.tostring(cmd).decode())
    input("Hit enter to continue: ")

## Exercise 7c ##
cfg_cmds = [
    "interface loopback73",
    "description LOOPBACK73",
    "interface loopback74",
    "description LOOPBACK74"
]

output = device.config_list(cfg_cmds)
for entry in output:
    print(etree.tostring(entry).decode())

