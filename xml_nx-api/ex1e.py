from lxml import etree
from ex1a import my_xml

# assign trust_zone the following:
# [<Element zones-security at 0x7f11927fee08>, <Element zones-security at 0x7f11927fed08>, <Element zones-security at 0x7f11927fee48>]
trust_zone = my_xml.getchildren()[0]
# assign child the following:
# <Element zones-security-zonename at 0x7ff69677f9c8># 
child = trust_zone.getchildren()[0]
# print the text associated with tag Element zones-security-zonename
print(child.text)
