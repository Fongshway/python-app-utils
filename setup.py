import os

from setuptools import find_packages
from setuptools import setup

# Package meta-data.
MAINTAINER = "Fongshway"
MAINTAINER_EMAIL = "8451964+Fongshway@users.noreply.github.com"
NAME = "app_utils"
REQUIRED = [
    "yapf",
]
SCRIPTS = [
    "bin/yapf-linter"
]
VERSION = None

here = os.path.abspath(os.path.dirname(__file__))

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


setup(
    name=NAME,
    version=about["__version__"],
    description="My utils for Python 3 applications",
    author=MAINTAINER,
    author_email=MAINTAINER_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    url="https://github.com/Fongshway/python-app-utils",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],
    packages=find_packages(exclude=("tests", "tests.*",)),
    install_requires=REQUIRED,
    scripts=SCRIPTS,
)
