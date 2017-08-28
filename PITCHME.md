---
#ns-3 App Store
---
## Final Product

An App Store for contributed ns-3 modules. This project will help in modularising the ns-3 codebase. Developers will be
able to use the App Store to advertise their apps. ns-3 Users will be able to download the modules according to their 
requirement from the Store. The project aims creates a web-interface for the App Store infrastructure. The website is made 
available to public at [ns-apps.ee.washington.edu](http://ns-apps.ee.washington.edu/).
---
## Contributions

The App Store for ns-3 has been designed from scratch. The frontend design of the website has been taken from [CyAppStore](apps.cytoscape.org). The backend has been made from scratch with the latest version of [Django](https://www.djangoproject.com/) to suit the ns-3 requirements.
* The Source Code is available [here](https://github.com/abhijithanilkumar/ns-3-AppStore). [[Contributions](https://github.com/abhijithanilkumar/ns-3-AppStore/graphs/contributors)]
* The design details and project progress over the summer is available [here](https://www.nsnam.org/wiki/GSOC2017AppStore).
---
## Setup and Usage

* Detailed documentation on setting up the App Store locally in your system, and to deploy it on a server is provided in the
[wiki](https://github.com/abhijithanilkumar/ns-3-AppStore/wiki).
* The user facing documentation for using the App Store is available [here](https://www.nsnam.org/~tomh/app-store-overview.pdf).
---
## Future Work

* Integrate the App Store with Bake. This can be done once the structure of the bakeconf.xml file for each module is finalised. Currently, the App Store has the ability to extract data from xml, using `xml.etree.ElementTree`. To create/edit modules with data from bake file, `src/util/parse_bake.py` file has to be modified to do the same. Then the `parse_xml` function has to be called from the appropriate view. 
* Integrate the web interface with the command-line. This can be done by creating APIs for the command-line tool to interact with using [Django Rest Framework](http://www.django-rest-framework.org/). Once this is done, the user should be able to install a module by the command `bake install <module-name>`
---
## Wrapping Up
I would like to thank my mentor, [Tom Henderson](https://github.com/tomhenderson) for guiding me during GSoC and providing me with constructive feedback during development. I thank all ns-3 developers who provided their feedback during the development of the website. I have built this website up from scratch, and I will be working post-GSoC to get the web-interface integrated with the command-line tool.

Cheers,
Abhijith.
---
