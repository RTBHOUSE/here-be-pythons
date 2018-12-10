.. _python_isort:

isort - Imports Sorter
======================

.. admonition:: Main point
   :class: tip

   Use `isort <https://github.com/timothycrosley/isort>`_ to automatically sort and group Python imports.


+ There are several knobs configuring isort's behavior. Full reference of settings can be found on `the isort wiki <https://github.com/timothycrosley/isort/wiki/isort-Settings#full-reference-of-isort-settings>`_.

+ You can specify project level configuration by placing ``.isort.cfg`` file at the root of your project.

    + An example of preconfigured ``.isort.cfg`` is in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/.isort.cfg>`_.

+ It is recommended to include isort in your linting Invoke task and also to run it during pre-commit Git hook. Example of both can be found in Big-Bang-py, see `tasks.py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks.py#L41-L46>`_ and `pre-commit <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/hooks/pre-commit#L36-L45>`_ files.

+ To manage edge cases, `disable isort per line or for entire file <https://github.com/timothycrosley/isort#skip-processing-of-imports-outside-of-configuration>`_.
