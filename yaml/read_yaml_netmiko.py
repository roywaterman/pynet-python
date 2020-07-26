import yaml

# Read device_list.yml into Python 
filename = device_list.yml
with open(filename) as f:
    yaml_out = yaml.load(f)

# Extract the dictionary elements from the outer list
device1 = yaml_out[0]
device2 = yaml_out[1]
device3 = yaml_out[2]
device4 = yaml_out[3]

# Add the device_type to the dictionaries
yaml_out[0]['device_type'] = 'cisco_nxos'
yaml_out[1]['device_type'] = 'cisco_nxos'
yaml_out[2]['device_type'] = 'cisco_ios'
yaml_out[3]['device_type'] = 'cisco_ios'

# Now each dictionary is ready to be used by Netmiko
net_connect = ConnectHandler(**device1)
print(net_connect.find.prompt())

net_connect = ConnectHandler(**device2)
print(net_connect.find.prompt())

net_connect = ConnectHandler(**device3)
print(net_connect.find.prompt())

net_connect = ConnectHandler(**device4)
print(net_connect.find.prompt())
