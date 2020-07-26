from lxml import etree
my_xml = etree.parse("show_security_zones.xml")
my_xml_string = etree.tostring(my_xml)
print(etree.fromstring(my_xml_string))
print(type(etree.fromstring(my_xml_string)))
