#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Timothy E Miller, PhD",
    author_email='timmil@cisco.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python module for handle NX-API communication with NX-OS switches",
    entry_points={
        'console_scripts': [
            'nxapi=nxapi.cli:main',
        ],
    },
    install_requires=requirements,
    license="Cisco Sample Code License, Version 1.1",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='nxapi',
    name='nxapi',
    packages=find_packages(include=['nxapi']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/gve-vse-tim/nxapi',
    version='0.1.0',
    zip_safe=False,
)
