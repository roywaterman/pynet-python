from lxml import etree
from ex1a import my_xml

etree.tostring(my_xml)
etree.tostring(my_xml).decode()
print(etree.tostring(my_xml).decode())


