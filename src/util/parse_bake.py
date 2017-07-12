import xml.etree.ElementTree as ET

def parse_xml(f):
    tree = ET.parse(f)
    root = tree.getroot()
    for child in root:
        print(child.tag, child.attrib)
