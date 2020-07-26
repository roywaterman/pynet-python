#!/usr/bin/env python
from pprint import pprint
from napalm import get_network_driver
from my_devices import network_devices


def connect(dev):
    device_type = dev.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**dev)
    device.open()
    return {'device': device, 'device_type': device_type}

if __name__ ==  "__main__":
    for entry in network_devices:
        output = connect(entry)
        print()
        print("Device facts")
        print("-" * len("Device facts"))
        facts = output['device'].get_facts()
        pprint(facts)
        print()
        print("Device type")
        print("-" * len("Device type"))
        print(output['device_type'])
        print()                
        print ("=" * 20)

