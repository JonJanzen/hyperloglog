#!/usr/bin/env python

from distutils.core import setup

version = '0.0.3'

setup(
    name='hyperloglog',
    version=version,
    maintainer='Jon Janzen',
    maintainer_email='jonjanzen@gmail.com',
    packages=['hyperloglog', 'hyperloglog.test'],
    license='LGPL',
    long_description=\
"""
Python implementation of the Hyper LogLog cardinality counter 
algorithms.

Using redis as the store

http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.76.4286
""",
)
