import os
import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices, output_printer
from pprint import pprint

def main():

    devices = yaml_load_devices()
    password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

    for name, device_dict in devices.items():
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip route")
        routes = output[0]['result']['vrfs']['default']['routes']
    for route, info in routes.items():
        if info['routeType'] == 'connected':
            print("Connected Route", "-", route)
        elif info['routeType'] == 'static':
            print("Static Route", "-", route)
        

if __name__ == "__main__":
    main()
