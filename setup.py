#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
from setuptools import setup, find_packages

version = os.environ['PACKAGE_VERSION']

requirements = ['pyspark',]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    name='mysparkpackage',
    author="Lace Lofranco",
    author_email='lace.lofranco@microsoft.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
    ],
    description="A nice python package!",
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(include=['mysparkpackage', 'mysparkpackage.core']),
    setup_requires=setup_requirements,
    test_suite='mysparkpackage.tests',
    tests_require=test_requirements,
    version=version
)
