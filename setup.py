#!/usr/bin/env python
from __future__ import print_function
 
import os
import sys
import subprocess

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

INFO = {
    'version': '0.0.1',
    }

def main():    
    packages = [
        'pystub', 
        ]
    pack_dir = {
        'pystub': 'pystub',
        }
    setup_kwargs = {
        "name": "pystub",
        "version": INFO['version'],
        # update the following:
        # "description": 'The Python Geographic Data Manipulation and Visualization Library',
        # "author": 'Matthew Gidden',
        # "author_email": 'matthew.gidden@gmail.com',
        # "url": 'http://github.com/gidden/pystub',
        "packages": packages,
        "package_dir": pack_dir,
        }
    rtn = setup(**setup_kwargs)

if __name__ == "__main__":
    main()

