from __future__ import unicode_literals, print_function
from lxml import etree
from pprint import pprint

with open("show_version.xml", "rb") as infile:
    # Parse string using etree.fromstring
    show_version = etree.fromstring(infile.read())

# Exercise 5a
# Print out the the namespace map of this XML object.
# You can accomplish this by using the .nsmap attribute of your XML object.

print(show_version.nsmap)

# Exercise 5b
# Use the find() method to access the text of the "proc_board_id" element (serial number).
# As this XML object contains namespace data, you will need to use the {*} namespace wildcard in the find() method
# Your find call should look as follows: find(".//{*}proc_board_id")

print(show_version.find(".//{*}proc_board_id").text) 
