import xml.etree.ElementTree as ET

def parse_xml(f):
    tree = ET.parse(f)
    root = tree.getroot()
    modules = []
    module_collection = root[0].tag
    for module in module_collection:
        modules.append(module)
    # Create/Edit Apps using the above data
