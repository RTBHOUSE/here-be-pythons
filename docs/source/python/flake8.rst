.. _python_flake8:

Flake8 - Octo-Ninja Linter
==========================

.. admonition:: Main point
   :class: tip

   Flake8 combines so much linter-power under the hood of a single tool! If used correctly, it will make your code not only more consistent, but simply better (and more pythonic 🐍).


+ `Flake8 <https://github.com/PyCQA/flake8>`_ is a wrapper around three tools:

    1. `PyFlakes <https://github.com/PyCQA/pyflakes>`_ - checks for Python errors.

    2. `pycodestyle <https://github.com/PyCQA/pycodestyle>`_ - tests Python code against some of the style conventions in `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_.

    3. `McCabe <https://github.com/PyCQA/mccabe>`_ - analyses Python code complexity (see the :ref:`next section <python_mccabe>` for more details).

+ Flake8 is configurable, where specific setup can be pointed in a `couple of ways <http://flake8.pycqa.org/en/latest/user/configuration.html>`_.

    + You may find preconfigured `.flake8 <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/.flake8>`_ in Big-Bang-py.

+ There is an abundance of `plugins <http://flake8.pycqa.org/en/latest/user/using-plugins.html>`_ greatly extending capability of Flake8. Search for them on `GitHub <https://github.com/search?q=flake8>`_.

    + A bunch of plugins are included in Flake8 configuration of Big-Bang-py. See all `flake8-*` packages in `dev.in <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/requirements/abstract/dev.in#L6-L14>`_ file.

    + An interesting example is `flake8-html <https://github.com/lordmauve/flake8-html>`_, which generates readable Flake8 HTML report (works similar to `coverage html`).

+ It is recommended to include Flake8 in your linting Invoke task and also to run it during Pre-commit Git Hook. Example of both can be found in Big-Bang-py, see `project.py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks/project.py#L40-L41>`_ and `Pre-commit <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/githooks/pre-commit#L61-L77>`_.

+ To manage edge cases, exclude Flake8 checking:

    1. `per code line <http://flake8.pycqa.org/en/latest/user/violations.html#in-line-ignoring-errors>`_;

    2. `per entire file <http://flake8.pycqa.org/en/latest/user/violations.html#ignoring-entire-files>`_;

    3. `per combination of file & error code <https://flake8.pycqa.org/en/latest/user/options.html?#cmdoption-flake8-per-file-ignores>`_;

    4. `per particular error <https://flake8.pycqa.org/en/latest/user/options.html?#cmdoption-flake8-ignore>`_.

    Option 3 & 4 are best set in `Flake8 config <http://flake8.pycqa.org/en/latest/user/configuration.html#project-configuration>`_. See an example below:

    .. code-block:: ini

        ignore =
            # C408: Unnecessary (dict/list/tuple) call - rewrite as a literal
            #
            # Calling directly dict/list/tuple is more obvious & explicit, making it
            # easier to read.
            C408,

            # C812 missing trailing comma
            #
            # Experience shows that this can be seriously inconvenient.
            C812

        per-file-ignores =
          ci/ci_checks.py: T001
          tasks/release.py: T001



