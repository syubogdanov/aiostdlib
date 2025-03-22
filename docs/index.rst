aiostdlib
=========

|PyPI Version| |PyPI Downloads| |License| |Python Version|

   [!WARNING] The library is in the pre-alpha stage. Bugs may exist!

Key Features
------------

-  Provides asynchronous version of the standard library;
-  The same API as the Python 3.13 standard blocking API;
-  Blocking IO is performed in a separate thread.

Getting Started
---------------

Installation
~~~~~~~~~~~~

The library is available as
`aiostdlib <https://pypi.org/project/aiostdlib/>`__ on PyPI:

.. code:: shell

   pip install aiostdlib

Usage
~~~~~

json
^^^^

For more, see the
`documentation <https://aiostdlib.readthedocs.io/en/latest/json.html>`__.

.. code:: python

   from aiostdlib import json

   async def main() -> None:
       with open("aiostdlib.json") as file:
           data = await json.load(file)

os
^^

For more, see the
`documentation <https://aiostdlib.readthedocs.io/en/latest/os.html>`__.

.. code:: python

   from aiostdlib import os

   async def main() -> None:
       fd = sys.stdout.fileno()
       detail = b"Hello, aiostdlib!"
       await os.write(fd, detail)

tomllib
^^^^^^^

For more, see the
`documentation <https://aiostdlib.readthedocs.io/en/latest/tomllib.html>`__.

.. code:: python

   from aiostdlib import tomllib

   async def main() -> None:
       with open("aiostdlib.toml", mode="rb") as file:
           data = await tomllib.load(file)

Documentation
-------------

.. toctree::
    :maxdepth: 1

    json
    tomllib

Environment
-----------

- If ``AIOSTDLIB_CONCURRENT_WORKERS`` is a positive integer, then no more than the specified number
  of threads will be used to execute calls asynchronously. If zero, then threading is not used at
  all. Otherwise, a minimum of ``32`` and ``os.cpu_count() + 4`` is the limit.

License
-------

MIT License, Copyright (c) 2025 Sergei Y. Bogdanov. See
`LICENSE <https://github.com/syubogdanov/aiostdlib/tree/main/LICENSE>`__
file.

.. |PyPI Version| image:: https://img.shields.io/pypi/v/aiostdlib.svg?color=green
   :target: https://pypi.org/project/aiostdlib/
.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/aiostdlib.svg?color=green
   :target: https://pypi.org/project/aiostdlib/
.. |License| image:: https://img.shields.io/pypi/l/aiostdlib.svg?color=green
   :target: https://github.com/syubogdanov/aiostdlib/tree/main/LICENSE
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/aiostdlib.svg?color=green
   :target: https://pypi.org/project/aiostdlib/
