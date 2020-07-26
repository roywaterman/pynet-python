from __future__ import unicode_literals, print_function
from lxml import etree
from pprint import pprint

with open("show_security_zones.xml", "r") as infile:
    # Parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

# Exercise 4a
# Use the find() method to retrieve the first "zones-security" element.
# Print out the tag of this element and of all its children elements.
print("Find tag of the first zones-security element")
print("-" * 20)
print(show_security_zones.find("zones-security").tag)
print()
print("Find tag of all child elements of the first zones-security element")
print("-" * 20)

# Note we can use getchildren() method with find method together
# This finds all the children elements under 1st instance of zones-security
elements = show_security_zones.find("zones-security").getchildren()

# As elements variable is a list, we can iterate using a for loop and print the tag of each child
for element in elements:
    print(element.tag)

print("\n\n")
# Exercise 4b
# Use the find() method to find the first "zones-security-zonename". 
# Print out the zone name for that element (the "text" of that element).
print("Find the first zones-security-zonename element, and print the text of that element")
print("-" * 20)
zonename = elements[0]
print(zonename.text)


print("\n\n")
# Exercise 4c
# Use the findall() method to find all occurrences of "zones-security".
# For each of these security zones, print out the security zone name ("zones-security-zonename", the text of that element).
print("For all the security zones, print out security zone name")
print("-" * 20)
all_zones = show_security_zones.findall("zones-security")
for zone_name in all_zones:
    print(zone_name[0].tag, "-", zone_name[0].text)





