#!/usr/bin/env python

import setuptools  # for side-effect to making "python setup.py develop" work
from distutils.core import setup

setup(name="inliner",
        version="1.0",
        description="Inline web assets automatically",
        author="John Evans",
        author_email="lgastako@gmail.com",
        py_modules=["inliner"],
        entry_points={
            "console_scripts": {
                "inline = inliner:main"
            }
        })