# -*- coding: utf-8 -*-

# Learn more: https://github.com/07ZonaM/Glacier.git

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='Glacier',
    
    description='Glacier Mapping',
    author='Various',
    author_email='test@test.com',
    url='https://github.com/07ZonaM/Glacier',
    install_requires=required,
    packages=find_packages(exclude=('web', 'ee_code', 'docs', 'conf', 'cluster'))
)


