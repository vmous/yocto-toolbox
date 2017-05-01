# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readmef = f.read()

with open('LICENSE') as f:
    licensef = f.read()

tests_require = [
    'networkx'
]

setup(
    name='yocto-toolbox',
    version='0.1.0',
    description='A set of scripts, utilities and libraries for automating every day _nix tasks.',
    long_description=readmef,
    author='Vassilis S. Moustakas',
    author_email='vsmoustakas@gmail.com',
    url='https://github.com/vmous/yocto-toolbox',
    license=licensef,
    packages=find_packages(exclude=('test', 'doc')),
    setup_requires=['pytest-runner'],
    tests_require=tests_require
)
