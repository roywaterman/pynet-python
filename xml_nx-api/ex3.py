from __future__ import unicode_literals, print_function
from pprint import pprint
import xmltodict

print("\n")
# Exercise 3a
with open("show_security_zones.xml") as filename:
    show_security_zones = xmltodict.parse(filename.read())

with open("show_security_zones_trust.xml") as filename:
    show_security_zones_trust = xmltodict.parse(filename.read())

print("\n\n")
print("Exercise 3b")
print("-" * 11)
zones = show_security_zones['zones-information']['zones-security']
trust = show_security_zones_trust['zones-information']['zones-security']
pprint(zones)
pprint(trust)
print(type(zones))
print(type(trust))

"""
print("\n\n")
print("Print the new variable and its type")
print("-" * 20)
pprint(show_security_zones)
print(type(show_security_zones))

print("\n\n")
print("Print out index and name of the security zones")
print("-" * 20)
zones = show_security_zones["zones-information"]["zones-security"]

# Note the f-string below (introduced in Python 3.6+)
for index, zone in enumerate(1, zones):
    print(f"Security Zone #{index}: {zone['zones-security-zonename']}")
print("\n\n")
"""
