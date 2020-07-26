#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from jnpr.junos import Device
from lxml import etree
from jnpr_devices import srx2
from getpass import getpass
from pprint import pprint

device = Device(**srx2)
device.open()

print("\n\n")
print("show version")
print("-" * len("show version"))
# show version | display xml rpc
# <get-software-information>
xml_out = device.rpc.get_software_information(normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))

print("\n\n")
print("show interfaces terse")
print("-" * len("show interfaces terse"))
# show interfaces terse | display xml rpc
# get-interface-information>
xml_out = device.rpc.get_interface_information(terse=True, normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))

print("\n\n")
print("show interfaces fe-0/0/7 terse")
print("-" * len("show interfaces fe-0/0/7 terse"))
# show interfaces fe-0/0/7 terse | display xml rpc
# get-interface-information>
xml_out = device.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))
