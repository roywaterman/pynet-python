from __future__ import unicode_literals, print_function
from pprint import pprint
import xmltodict

print("\n")

with open("show_security_zones_trust.xml") as filename:
    show_security_zones_trust = xmltodict.parse(filename.read(), force_list={"zones-security": True})

trust = show_security_zones_trust['zones-information']['zones-security']
pprint(trust)
print(type(trust))

