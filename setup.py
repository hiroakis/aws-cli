#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

import os
import sys
import awscli

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup

packages = [
    'awscli',
]

requires = ['botocore>=0.7.0',
            'six>=1.1.0',
            'argparse>=1.1']


setup(
    name='awscli',
    version=awscli.__version__,
    description='Universal Command Line Environment for AWS.',
    long_description=open('README.md').read(),
    author='Mitch Garnaat',
    author_email='garnaat@amazon.com',
    url='http://aws.amazon.com/cli/',
    scripts=['bin/aws', 'bin/aws.cmd',
             'bin/aws_completer', 'bin/aws_zsh_completer.sh'],
    packages=packages,
    package_data={'awscli': ['data/*.json']},
    package_dir={'awscli': 'awscli'},
    include_package_data=True,
    install_requires=requires,
    license=open("LICENSE.txt").read(),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
    ),
)
