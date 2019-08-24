import xml.etree.ElementTree as ET
from django.conf import settings


def parse_xml(f):
    tree = ET.parse(f)
    root = tree.getroot()
    modules = []
    module_collection = root[0].tag
    for module in module_collection:
        modules.append(module)
    # Create/Edit Apps using the above data


def get_dependency(app, latest_release):
	if latest_release:
		bakefile_url = settings.MEDIA_URL + str(latest_release.filename)
		data = latest_release.filename.read()
		tree = None
		try:
			tree = ET.fromstring(data)
		except:
			print("Error Parsing the XML File")
			return None, None
		root = tree.findall('modules')
		optional_dependency = []
		compulsory_dependency = []
		for modules in root:
			for module in modules:
				for dependency in module.findall('depends_on'):
					if dependency.attrib['optional'] == "True":
						optional_dependency.append(dependency.attrib['name'])
					elif dependency.attrib['optional'] == "False":
						compulsory_dependency.append(dependency.attrib['name'])
		return compulsory_dependency, optional_dependency
	else:
		return None, None