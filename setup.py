import os
from setuptools import setup, find_packages


lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = []

# Obtain list of requirements
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name='glpi-provider',
    version='0.1.4',
    license='MIT License',
    author='Tatianno Alves',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='tferreiraalves@gmail.com',
    keywords='glpi provider api rest',
    description=u'GLPI API Abstraction Layer',
    packages=find_packages(include=['glpi_provider', 'glpi_provider.*']),
    install_requires=install_requires,
)