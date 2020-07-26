import xmltodict
from pprint import pprint

with open("show_security_zones.xml", "r") as infile:
    show_security_zones = infile.read().strip()

zones_dict = xmltodict.parse(show_security_zones)

print()
print("Exercise 2a")
print("-" * 11)
# Using xmltodict, load the show_security_zones.xml file as a Python dictionary. 
# Print out this new variable and its type. 
# Note, the newly created object is an OrderedDict; not a traditional dictionary.
pprint(zones_dict)
print()
print(type(zones_dict))
print("\n\n")

print("Exercise 2b")
print("-" * 11)
# Print the names and an index number of each security zone in the XML data from Exercise 2a. 
# Your output should look similar to the following (tip, enumerate will probably help):

zones = zones_dict['zones-information']['zones-security']
counter = 1
for zone in zones:
    print("Security Zone", "#"+str(counter)+":", (zone['zones-security-zonename']))
    counter +=1
