
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

setup(
    name='namegen',
    version='0.0.1',
    description='Personal name generation script. Copies to clipboard and echos results.',
    long_description=readme,
    author="Eoin O'Neill",
    author_email="eoinoneill1991@gmail.com",
    url = '',
    py_modules = ['namegen'],
    license = license,
    install_requires = [requirements],
    packages = find_packages(),
    entry_points = '''
        [console_scripts]
        namegen=namegen:entry
    '''
)
