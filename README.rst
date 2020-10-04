asyncpokepy
===========

.. image:: https://www.smogon.com/forums/attachments/zeraora-gif.247599/
    :height: 50px
    :target: https://pypi.python.org/pypi/asyncpokepy
    :alt: Zeraora

.. image:: https://img.shields.io/pypi/v/asyncpokepy.svg
    :target: https://pypi.python.org/pypi/asyncpokepy
    :alt: Latest PyPI version

.. image:: https://img.shields.io/badge/license-MIT-yellowgreen
    :target: https://mit-license.org
    :alt: MIT License link

.. image:: https://img.shields.io/badge/python-3.6%2B-blue
    :target: https://www.python.org/downloads/
    :alt: Python version 3.6 and above

An asynchronous Python API wrapper for the PokéAPI

Installation
------------
MacOS / Linux:

.. code:: sh

    python3 -m pip install -U asyncpokepy

Windows:

.. code:: sh

    py -3 -m pip install -U asyncpokepy

Usage
-----
You must create an instance of the pokeclient in order to utilise its functionality:

.. code:: py

    from asyncpokepy import pokeclient
    pokeclient = pokeclient()

Examples
--------
These examples assume you have created an instance as above.

.. code:: py

    async def getpikachu():
        # This will return an object, setting object to False will return a dictionary
        return pokeclient.getpokemon('pikachu', object=True)

Output:

.. code:: py

    <asyncpokepy.objects.Pokemon object at 0x7fa4bb929580>

Authors
-------

`asyncpokepy` was written by `Raj Sharma <yrsharma@icloud.com>`_.

`PokéAPI` was constructed by `Paul Hallett <https://github.com/phalt>`_.
