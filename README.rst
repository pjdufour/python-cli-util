Python CLI Util (python-cli-util)
==========

.. image:: https://travis-ci.org/pjdufour/python-cli-util.png
    :target: https://travis-ci.org/pjdufour/python-cli-util

.. image:: https://img.shields.io/pypi/v/python-cli-util.svg
    :target: https://pypi.python.org/pypi/python-cli-util

.. image:: https://readthedocs.org/projects/python-cli-util/badge/?version=master
        :target: http://python-cli-util.readthedocs.org/en/latest/
        :alt: Master Documentation Status

Description
-----------

A python utility library for command line interaction.

Installation
------------

.. code-block:: bash

    pip install git+git://github.com/pjdufour/python-cli-util.git@master

Usage
-----

.. code-block:: python

    from  pythoncliutil import request_input, request_continue

    value = request_input(question, value, required, options=None)
    request_continue()
    #
    value = request_input("Which letter?", None, True, options=['a','b','c'])

Contributing
------------

We are currently accepting pull requests for this repository. Please provide a human-readable description with a pull request and update the README.rst file as needed.

License
-------

Copyright (c) 2015, Patrick Dufour
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of python-cli-util nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
