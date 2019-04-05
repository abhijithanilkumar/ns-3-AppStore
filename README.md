

# ns3 App Store

ns3 App Store is a is a web application for a module database in ns-3. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* accounts (handles user accounts - Sign In, Sign Up etc.)
* profiles (handles user profiles)
* appstore (handles core details of the web app)
* help (handles static pages like about, contact us)
* search (handles free text searching)
* apps (handles navigation of apps)
* backend (handles upload and bake integration of apps)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv appstore`
    2. `$ . appstore/bin/activate`

Install all dependencies:

    1. Move to the folder 'ns-3-Appstore' in which the file 'requirements.txt' is present
    2. pip install -r requirements.txt

Set up the environment:

    1. cd src/appstore/settings/
    2. cp local.sample.env local.env

Run migrations:
    1. Move to the folder 'src' in which the file 'manage.py' is present
    2. python manage.py makemigrations
    3. python manage.py migrate

### Detailed instructions

Take a look at the [wiki][2]/docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: https://github.com/abhijithanilkumar/ns-3-AppStore/wiki