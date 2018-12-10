.. _python_pipenv:

Pipenv - App Package Manager
============================

.. admonition:: Main point
   :class: tip

   Use `Pipenv <https://pipenv.readthedocs.io/en/latest>`_ to manage Python `app dependencies <https://pipenv.readthedocs.io/en/latest/advanced/#pipfile-vs-setup-py>`_.


+ **Pipenv** consolidates ``pip`` & ``virtualenv`` while offering powerful new features. Among others:

    + Virtual environment is created and managed automatically.

    + Project dependencies are installed using ``Pipfile`` (building from the latest allowed versions of packages) or ``Pipfile.lock`` (making builds deterministic):

        + ``Pipfile`` specifies only the packages you need, as those are abstract dependency declarations. Sub-dependencies are taken care of by Pipenv.

        + ``Pipfile.lock`` uses hashes to lock all of the dependencies (including sub-dependencies). This ensures repeatable, deterministic builds. You never manage this file by hand, leaving the matter for Pipenv.

        + You may find an example of Pipfile in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/tree/master/%7B%7Bcookiecutter.project_dir%7D%7D/Pipfile>`_.

+ Essential commands:

    + ``install`` - installs provided packages and adds them to Pipfile. If no packages are given, installs all packages from ``Pipfile``.

    + ``sync`` - deterministic build! Installs all packages specified in ``Pipfile.lock``.

    + ``shell`` - spawns a shell with the virtualenv activated.

        + `Shell environment will be automatically updated with ENVs from .env file <https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-automatic-loading-of-env>`_.

    + ``run`` - runs a given command from the virtualenv with forwarded arguments.

        + `Shell environment will be automatically updated with ENVs from .env file <https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-automatic-loading-of-env>`_.

    + ``graph`` - shows a dependency graph of the installed dependencies.

    + ``check`` - most importantly, checks for security vulnerabilities.

+ You can educate yourself further by reading `Real Python's guide <https://realpython.com/pipenv-guide>`_. It is also recommended to go through `the official documentation <https://pipenv.readthedocs.io/en/latest/#further-documentation-guides>`_.
