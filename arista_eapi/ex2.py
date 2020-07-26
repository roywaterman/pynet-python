import pyeapi
import yaml # importing yaml module
from getpass import getpass
import myfuncs

read_yaml()
device_dict['password'] = getpass()

connection = pyeapi.client.connect(**device_dict)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

output_data()




