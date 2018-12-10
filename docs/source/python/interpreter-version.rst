.. _python_python_version:

Interpreter Version
===================

.. admonition:: Main point
   :class: tip

   It is recommended to use Python 3.7.


+ There is an informative summary of new features on `Real Python <https://realpython.com/python37-new-features>`_. More detailed description can be found in `the official documentation <https://docs.python.org/3/whatsnew/3.7.html>`_.

+ To name some notable additions:

    + `Data Classes <https://realpython.com/python-data-classes>`_ can easily replace `namedtuples <https://docs.python.org/3.7/library/collections.html#collections.namedtuple>`_ and `attrs <https://github.com/python-attrs/attrs>`_.

    + `Typing Forward Reference <https://realpython.com/python37-new-features/#typing-enhancements>`_ makes type hints even more programmer-friendly.

    + The "asyncio" module has received many `new features along with usability and performance improvements <https://tryexceptpass.org/article/asyncio-in-37/>`_. For instance, new "asyncio.run()" automatically creates an event loop, runs a task on it and finally closes the loop when the task is done.

+ Nonetheless, if you still use previous version of Python (especially 3.6), it is possible to backport some of the new features e.g. `Data Classes <https://github.com/ericvsmith/dataclasses>`_.
