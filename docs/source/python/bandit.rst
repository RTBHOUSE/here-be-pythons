.. _python_flake8:

Bandit - Find Security Issues
=============================

.. admonition:: Main point
   :class: tip

    Bandit will report security issues in Python code that might have slipped off your attention.


+ `Bandit <https://github.com/PyCQA/bandit>`_ is a tool designed to find common security issues in Python code.

+ To run Bandit from the shell, simply call:

  .. code-block:: shell

      bandit --recursive .

  Details about more advanced usage can be found in `Bandit README <https://github.com/PyCQA/bandit#usage>`_.

+ Bandit is configurable via `.bandit <https://github.com/PyCQA/bandit#per-project-command-line-args>`_ file.

    + You may find preconfigured `.bandit <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/.bandit>`_ in Big-Bang-py.

+ It is recommended to include Bandit in your linting Invoke task and also to run it during Pre-commit Git Hook & CI. Example of both can be found in Big-Bang-py, see `project.py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks/project.py#L43-L45>`_ and `ci_checks.py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/ci/ci_checks.py#L74-L84>`_.

+ To manage edge cases, exclude Bandit checking `per line <https://github.com/PyCQA/bandit#exclusions>`_.
