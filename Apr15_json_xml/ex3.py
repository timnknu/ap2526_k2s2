import xml.etree.ElementTree as ET

fname = '/home/tniko/tmp/MECHMAT/AP_25-26/sem2/json_xml/document.xml'
#fname = 'xml_ex1.xml'

tree = ET.parse(fname)
root = tree.getroot()
# for e in root.iter():
#     print('--------------------')
#     print(e.tag)
#     print(e.text)
#     print(e.attrib)

# r = root.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
# print(r)

# def prettyprint(elem, indent):
#     print(indent, elem.tag)
#     for e in elem.findall('*'):
#         prettyprint(e, indent+ '  ')
# prettyprint(root, '')

#

r = root.find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
print(r)