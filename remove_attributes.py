import sys
import xml.etree.ElementTree as ET

input_file = sys.argv[1]
output_file = sys.argv[2]

tree = ET.parse(input_file)
root = tree.getroot()

for elem in root.iter():
    elem.attrib.pop('DisableRemoteExpand', None)
    elem.attrib.pop('DisableRemoteToggle', None)

tree.write(output_file, encoding='utf-8', xml_declaration=True)