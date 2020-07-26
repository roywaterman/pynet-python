from lxml import etree
from ex1a import my_xml

print()
print()
print()

# get child elements of my_xml
children = my_xml.getchildren()
print(children)

# children variable is a list, to get 1st element just use [0]
first_child = children[0]

# print tag
print(first_child.tag)
