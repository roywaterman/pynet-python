from lxml import etree
from ex1a import my_xml

# assign trust_zone the following:
# [<Element zones-security at 0x7f11927fee08>, <Element zones-security at 0x7f11927fed08>, <Element zones-security at 0x7f11927fee48>]
trust_zone = my_xml.getchildren()[0]
 
children = trust_zone.getchildren()
for child in children:
    print(child.tag)


