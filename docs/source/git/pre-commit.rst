.. _git_precommit:

Pre-commit Git Hook
===================

.. admonition:: Main point
   :class: tip

   The Pre-commit `Git Hook <https://githooks.com>`_ is run - surprise, surprise - before you commit! 😀 It is a perfect opportunity to run tests and linters.


+ Regardless of your discipline as a software programmer or simply how good is your memory, Pre-commit Git Hook will check your code automatically. In effect:

    + Your code stays consistent and readable.

    + All while keeping to pass both new and regression tests.

+ Pre-commit Git Hook is a match made in heaven when combined with properly configured :ref:`Continuous Integration<project_ci>`. It can save you a lot of time (and nerves!) when you have a solid opportunity to fail the checks locally i.e. before being officially rejected by your hosted VSC provider.

+ You can find an example of Pre-commit Git Hook in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/githooks/pre-commit>`_.

    + ``set_precommit`` Invoke task in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks/project.py#L48-L58>`_ takes your Pre-commit Git Hook from ``/githooks/pre-commit`` and automatically sets it up for you.

