import os
from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), 'rb') as f:
    long_description = f.read().decode('utf-8')

setup(
	name = "fastly-python",
	version = "1.0.4-wikia-pypi-test1",
	author = "Chris Zacharias",
	author_email = "chris@imgix.com",
	description = ("A Python client libary for the Fastly API."),
	license = "BSD",
	keywords = "fastly",
	url = "https://github.com/zebrafishlabs/fastly-python",
	packages=['fastly', 'tests'],
	scripts=['bin/fastly_upload_vcl.py', 'bin/fastly_purge_url.py'],
	long_description=long_description,
        install_requires=['httplib2'],
        classifiers=[
		"Development Status :: 3 - Alpha",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"License :: OSI Approved :: BSD License",
	],
)
