from setuptools import setup


install_requires = []

with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name='glpi_provider',
    version='0.0.1',
    license='MIT License',
    author='Tatianno Alves',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='tferreiraalves@gmail.com',
    keywords='glpi provider api rest',
    description=u'GLPI API Abstraction Layer',
    packages=['glpi_provider'],
)