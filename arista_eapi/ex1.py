import pyeapi
from getpass import getpass
from pprint import pprint

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

device = pyeapi.client.Node(connection)
output = device.enable(["show ip arp"])
addresses = output[0]['result']['ipV4Neighbors']

for entry in addresses:
    print(entry['hwAddress'], "-", entry['address'])
