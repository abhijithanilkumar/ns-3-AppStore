---
# ns-3 App Store
---
## Final Product

An App Store for contributed ns-3 modules. This project will help in modularising the ns-3 codebase. Developers will be
able to use the App Store to advertise their apps. ns-3 Users will be able to download the modules according to their 
requirement from the Store. The project created a web-interface for the App Store infrastructure.
+++
![Home](https://github.com/abhijithanilkumar/Images-ns3-AppStore/blob/master/home.jpg)
---
## Work Done

* Created a dummy Django Project using [Edge](https://django-edge.readthedocs.io/en/latest/).
* Integrated the Edge project with frontend code from [Cytoscape](https://github.com/cytoscape/appstore).
* Designed the backend for the ns-3 App Store according to the requirements.
* Integrated Edge, Cytoscape Design (uses [Bootstrap](http://getbootstrap.com/)) and the newly designed backend to work with the latest version of Django and dependent packages.
* Deployed the site using Gunicorn and Nginx.
---
## Contributions

* The Source Code is available [here](https://github.com/abhijithanilkumar/ns-3-AppStore). 
* The base project was created using [Edge](https://django-edge.readthedocs.io/en/latest/) and the frontend code is taken from [CyAppStore](https://github.com/cytoscape/appstore).
* Backend design, integration of different components and deployment of the website was done during GSoC. ([Contributions](https://github.com/abhijithanilkumar/ns-3-AppStore/graphs/contributors))
* The design details and project progress over the summer is available [here](https://www.nsnam.org/wiki/GSOC2017AppStore).
---
## Setup and Usage

* Detailed documentation on setting up the App Store locally in your system, and to deploy it on a server is provided in the
[wiki](https://github.com/abhijithanilkumar/ns-3-AppStore/wiki).
* A draft of the user facing documentation for using the App Store is available in the project demonstration site and is accessible from the wiki.
---
## Future Work

* Integrate the App Store with Bake. Bake is the build orchestration tool used in ns-3. Bake uses XML to describe modules. By using a standardized XML schema that describes an ns-3 module, it can be used in both the app store and also in bake. Once integrated, the App Store will be able to retrieve data from the xml file and the data will be autopopulated.  
+++
* Bake integration can be done once the structure of the bakeconf.xml file for each module is finalised. Currently, the App Store has the ability to extract data from xml, using `xml.etree.ElementTree`. To create/edit modules with data from bake file, `src/util/parse_bake.py` file has to be modified to do the same. Then the `parse_xml` function has to be called from the appropriate view. 
+++
* Integrate the web interface with the command-line. This can be done by creating APIs for the command-line tool to interact with using [Django Rest Framework](http://www.django-rest-framework.org/). Once this is done, the user should be able to install a module by the command `bake install <module-name>`
---
## Wrapping Up
I would like to thank my mentor, [Tom Henderson](https://github.com/tomhenderson) for guiding me during GSoC and providing me with constructive feedback during development. I thank all ns-3 developers who provided their feedback during the development of the website. I have built this website up from scratch, and I will be working post-GSoC to get the web-interface integrated with the command-line tool.
