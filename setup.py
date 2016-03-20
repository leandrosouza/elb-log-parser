#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-log-parser.
# https://github.com/leandrosouza/elb-log-parser

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Leandro Souza <lsouzarj@gmail.com>

from setuptools import setup, find_packages
from elb_log_parser import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
]

setup(
    name='elb-log-parser',
    version=__version__,
    description='AWS Elastic Load Balancing log parser.',
    long_description='''
AWS Elastic Load Balancing log parser.
''',
    keywords='AWS Elastic Load Balancing log parser python',
    author='Leandro Souza',
    author_email='lsouzarj@gmail.com',
    url='https://github.com/leandrosouza/elb-log-parser',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'six>=1.9.0,<2.0.0',
        'user-agents>=1.0.0,<2.0.0',
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'elb-log-parser=elb_log_parser.cli:main',
        ],
    },
)
