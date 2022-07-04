from setuptools import find_packages, setup

__version__ = "0.0.1"

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="pycollections",
    version=__version__,
    author="Felix Etzkorn",
    author_email="felix.etzkorn@web.de",
    description="A package with different implementations for lists, sets and maps",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ftjahn8/pycollections/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha"
        "Intended Audience :: Developers"
        "Natural Language :: English"
        "Programming Language :: Python"
        "Programming Language :: Python :: 3"
        "Programming Language :: Python :: 3 :: Only"
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
