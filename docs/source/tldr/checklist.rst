.. _tldr_checklist:


TL;DR Checklist
===============

+ Python:

    + Use `Python 3.7 <https://docs.python.org/3/whatsnew/3.7.html>`_.

    + Manage app dependencies using a combo of `virtualenv <https://virtualenv.pypa.io/en/latest/>`_ and `pip-tools <https://github.com/jazzband/pip-tools>`_.

    + Sort imports with `isort <https://github.com/timothycrosley/isort>`_.

    + Format source files with `YAPF <https://github.com/google/yapf>`_.

    + Lint code with `Flake8 <https://github.com/PyCQA/flake8>`_.

    + Check security issues with `Bandit <https://github.com/PyCQA/bandit>`_.

    + Use `pytest <https://docs.pytest.org/en/latest/>`_ as test framework.

+ Git:

    + Use `.gitignore <https://git-scm.com/docs/gitignore>`_.

    + Use `Pre-commit Git Hook <https://githooks.com>`_.

+ Project:

    + Store config  (credentials, secrets, etc.) in `the environment <https://12factor.net/config>`_.

    + Manage and execute command line tasks via `Invoke <http://www.pyinvoke.org>`_.

    + `Log, log, log. <https://realpython.com/python-logging/>`_

    + Maintain up-to-date `README <https://www.makeareadme.com>`_.

    + Set up `Continuous Integration <https://docs.microsoft.com/en-us/azure/devops/learn/what-is-continuous-integration>`_.
