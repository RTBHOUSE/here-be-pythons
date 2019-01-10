.. _git_precommit:

Pre-commit Git Hook
===================

.. admonition:: Main point
   :class: tip

   The pre-commit `Git hook <https://githooks.com>`_ is run before you even start typing new commit message. It is a perfect opportunity to run tests and linters.


+ Regardless of your discipline as a software programmer or simply how good is your memory, pre-commit Git hook will check your code automatically. In effect:

    + Your code stays consistent and readable.

    + All while keeping to pass both new and regression tests.

+ Pre-commit Git hook is a match made in heaven when combined with properly configured :ref:`Continuous Integration<project_ci>`. It can save you a lot of time (and nerves!) when you have a solid opportunity to fail the checks locally i.e. before being officially rejected by your hosted VSC provider.

+ You can find an example of pre-commit Git hook in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/githooks/pre-commit>`_.

    + ``install_precommit`` Invoke task in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks.py#L27-L35>`_ takes your pre-commit Git Hook from ``/githooks/pre-commit`` and automatically sets it up for you.

