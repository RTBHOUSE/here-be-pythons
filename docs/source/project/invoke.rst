.. _project_invoke:

Invoke - Manage & Execute Tasks
===============================

.. admonition:: Main point
   :class: tip

   Turn into a task every project related shell command which will be called more than a couple of times and is not super-common (like ``ls`` with basic flags).

   Manage and execute those project tasks via `Invoke <http://www.pyinvoke.org>`_.

+ You can replace ``Makefiles`` and similar straightaway, as Invoke is dead simple.

+ Invoke tasks are called by typing in the shell ``invoke *task-name*``.

+ Invoke tasks are normal Python functions organised in ``tasks.py`` file.

+ Docstrings of functions implementing Invoke tasks are automatically formatted into a command line help:


.. code-block:: txt

    >>> invoke --list
    Available tasks:

      task1   First line of task1 docstring.
      task2   First line of task2 docstring.

    >>> invoke --help task2
    Usage: inv[oke] [--core-opts] task2 [--options] [other tasks here ...]

    Docstring:
      Full docstring of task 2.

    Options:
      -p TYPE, --param=TYPE   Your additional parameters help string.


.. note::

   To learn how to add help for additional parameters for Invoke tasks, see `the docs <http://docs.pyinvoke.org/en/0.11.0/getting_started.html#adding-help-for-parameters>`_.


+ `Invoke tasks can be organised using namespaces <http://docs.pyinvoke.org/en/1.2/concepts/namespaces.html>`_. Then, for instance, you can call server tasks like ``server.deploy``/``server.logs`` or organise job-related tasks like ``job.start``/``job.stop``.

+ Invoke can be easily buffed with `shell tab completion <http://docs.pyinvoke.org/en/1.2/invoke.html#shell-tab-completion>`_.

    + If you work on your projects using ``bash`` with virtualenv loaded via ``pipenv shell``, a ready-2-go installation script can be found in the file ``invoke_bash_completion`` in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/invoke_bash_completion>`_. If your development environment differs, this script can still give you a basis, or at least a hint, how to build a solution of your own.

+ You may find examples of Invoke tasks in the ``tasks.py`` in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks.py>`_.

+ `The official documentation <http://docs.pyinvoke.org/en/1.2/>`_ is solid. Get familiar with it.
