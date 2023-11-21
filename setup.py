
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='namegen',
    version='0.0.1',
    description='Personal name generation script. Copies to clipboard and echos results.',
    long_description=readme,
    author="Eoin O'Neill",
    author_email="eoinoneill1991@gmail.com",
    url='',
    license=license,
    packages=find_packages("namegen"),
    entry_points = {
              'console_scripts': [ 'namegen = src.namegen:entry' ],
          },
)
