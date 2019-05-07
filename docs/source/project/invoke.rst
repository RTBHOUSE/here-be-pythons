.. _project_invoke:

Invoke - Manage & Execute Tasks
===============================

.. admonition:: Main point
   :class: tip

   Turn into a task every project related shell command which will be called more than a couple of times and is not super-common (like ``ls`` with basic flags).

   Manage and execute those project tasks via `Invoke <http://www.pyinvoke.org>`_.

+ You can replace ``Makefiles`` and similar task managers straightaway as Invoke is intuitive and user-friendly.

+ Invoke tasks are called by typing in the shell ``invoke *task-name*``.

    + Invoke can be easily buffed with `shell tab completion <http://docs.pyinvoke.org/en/1.2/invoke.html#shell-tab-completion>`_.

      If you work on your projects using ``bash`` with virtualenv, a ready-2-go installation script can be found in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/invoke_bash_completion>`_. If your development environment differs, this script can still give you a basis, or at least a hint, how to build a solution of your own.

+ Invoke tasks are normal Python functions organised in ``tasks.py`` file or `tasks Python package <https://github.com/RTBHOUSE/big-bang-py/tree/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks>`_.

    + You may find examples of Invoke tasks in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks.py>`_.

+ Docstrings of functions implementing Invoke tasks are automatically formatted into a command line help:

    .. code-block::  console

        > invoke --list
        Available tasks:

          task1   First line of task1 docstring.
          task2   First line of task2 docstring.

        > invoke --help task2
        Usage: inv[oke] [--core-opts] task2 [--options] [other tasks here ...]

        Docstring:
          Full docstring of task 2.

        Options:
          -p TYPE, --param=TYPE   Your additional parameters help string.


    .. note::

       To learn how to add help for additional parameters for Invoke tasks, see `the docs <http://docs.pyinvoke.org/en/0.11.0/getting_started.html#adding-help-for-parameters>`_.


+ `Invoke tasks can be organised using namespaces <http://docs.pyinvoke.org/en/1.2/concepts/namespaces.html>`_. For instance:

    .. code-block::  python

        # File: $PROJECT_ROOT/tasks.py

        import invoke

        import src.app.tasks
        import src.db.tasks


        @invoke.task
        def core_task_1(c):
            pass


        @invoke.task
        def core_task_2(c):
            pass


        ##################################
        # Organise tasks into namespaces #
        ##################################

        # Because we are customizing tasks, now we HAVE TO manually create
        # main namespace and point to it via variable named `namespace` or `ns`.
        # See: http://docs.pyinvoke.org/en/1.2/concepts/namespaces.html#starting-out
        namespace = invoke.Collection()

        # Add to the main namespace top-level tasks from the current file.
        namespace.add_task(core_task_1)
        namespace.add_task(core_task_2)

        # Create `app` namespace and add related tasks.
        app_namespace = invoke.Collection('app')
        app_namespace.add_task(src.app.tasks.start)
        app_namespace.add_task(src.app.tasks.stop)

        # Create `db` namespace and add related tasks.
        db_namespace = invoke.Collection('db')
        # By default task name will be derived from the implementing function
        # name, but we can also customize it via `aliases` argument.
        db_namespace.add_task(src.db.tasks.fire_up_postgres, aliases='fire_up')
        db_namespace.add_task(src.db.tasks.stop_postgres, aliases='stop')
        # We can nest `db` namespace into `app` namespace!
        app_namespace.add_collection(db_namespace)

        # Finally, we have to add `app` namespace (together with the nested
        # `db` tasks) to the main namespace.
        namespace.add_collection(app_namespace)

    Now we can call our tasks like ``app.start`` or ``app.db.fire-up``. Sweet!

+ If Invoke task behaves weirdly regarding prints/logs/stdout/stderr/etc. it is worth trying to add ``pty=True`` argument in ``c.run`` call:

    .. code-block::  python

        @invoke.task
        def flake8(c):
            c.run('python -m flake8', pty=True)

    By default, ``run`` connects directly to the invoked process and reads its stdout/stderr streams. Some programs will behave differently in this situation compared to using an actual terminal or pseudoterminal (pty). Due to their nature, ptys have a single output stream, so the ability to tell stdout apart from stderr is not possible. As such, all output will appear on ``out_stream`` and be captured into the ``stdout`` result attribute. ``err_stream`` and ``stderr`` will always be empty when ``pty=True``.

+ `The official documentation <http://docs.pyinvoke.org/en/1.2/>`_ is solid. Get familiar with it.
