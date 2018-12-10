.. _cookiecutter_yapf:

YAPF - Source Code Formatter
============================

.. admonition:: Main point
   :class: tip

   `YAPF <https://github.com/google/yapf>`_'s goal is to make Python code look as good as written by a programmer who is rigorously following a style guide. Make it your linter of choice.


+ The formatting style used by YAPF is configurable, where specific configuration can be pointed in a couple of ways.

    + It is recommended to store the configuration in a properly formatted ``.style.yapf`` file at the root of your project.

    + You may find pre-configured ``.style.yapf`` in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/.style.yapf>`_.

+ It is recommended to include YAPF in your linting Invoke task and also to run it during pre-commit Git hook. Example of both can be found in Big-Bang-py, see `tasks.py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks.py#L48-L52)>`_ and `pre-commit <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/hooks/pre-commit#L47-L59>`_.

+ Survival tips:

    + If you leave trailing comma in a collection (be it a list, function parameters, etc.), YAPF will force it to break, giving one element per line.

    + YAPF is not perfect - from time to time you WILL see weirdly formatted code. There are at least two major occurrences:

        + Deeply Nested Dicts - this is quite understandable as decisions that improve readability are usually arbitrary and should be solved on a case-by-case basis.

        + Complex Comprehensions - comprehensions are split over multiple lines only when they exceed the column limit... This issue is brought to the attention of both YAPF authors (see issue on `Github <https://github.com/google/yapf/issues/628>`_) and other programmers (see posts on `Reddit <https://www.reddit.com/r/Python/comments/9mov4r/is_there_a_way_to_force_yapf_to_always_splitfold>`_) and `Stack Overflow <https://stackoverflow.com/questions/52558919/is-there-a-way-to-force-yapf-to-always-split-fold-comprehensions>`_).

    + To manage edge cases, `disable YAPF per line or per block <https://github.com/google/yapf#why-does-yapf-destroy-my-awesome-formatting>`_.
