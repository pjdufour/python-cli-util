#!/usr/bin/env python

from setuptools import setup

setup(
    name='python-cli-util',
    version='0.0.1',
    install_requires=[],
    author='Patrick Dufour',
    author_email='pjdufour.dev@gmail.com',
    license='BSD License',
    url='https://github.com/pjdufour/python-cli-util/',
    keywords='python',
    description='A python utility library for command line interaction.',
    long_description=open('README.rst').read(),
    download_url="https://github.com/pjdufour/python-cli-util/zipball/master",
    packages=[
        "pythoncliutil"],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
