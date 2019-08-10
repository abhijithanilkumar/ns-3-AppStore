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
	bakefile_url = settings.MEDIA_URL + str(latest_release.filename)
	# TODO: Write logic to get the dependencies from the bakefile
	return None