.. _python_mccabe:

McCabe - Code Complexity Checker
================================

.. admonition:: Main point
   :class: tip

   Library `McCabe <https://github.com/pycqa/mccabe>`_ automatically detects over-complex code basing on cyclomatic complexity.


+ Cyclomatic complexity is approximately equivalent to one plus the number of "loops and if statements". The simple interpretation is that it shows an upper bound for the number of test cases required to obtain branch coverage of the code, therefore it roughly indicates the effort required for writing tests.

    + Additional explanations can be found on `tutorialspoint <https://www.tutorialspoint.com/software_testing_dictionary/cyclomatic_complexity.htm>`_ and `Wikipedia <https://en.wikipedia.org/wiki/Cyclomatic_complexity>`_.

+ Code with high cyclomatic complexity (usually assumed as 10+) is likely to be difficult to understand and therefore have a higher probability of containing defects.

+ It is recommended to include McCabe in your linting Invoke task and also to run it during Pre-commit Git Hook. In Big-Bang-py McCabe is run automatically by Flake8 linter.

    + Cut-off complexity in Invoke task and Pre-commit Git Hook is arbitrarily assumed to be 7 (configured by `max-complexity <http://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-max-complexity>`_ set in `.flake8 <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/.flake8#L43-L44>`_). However, this number should be adjusted to reflect your experience and project needs.
