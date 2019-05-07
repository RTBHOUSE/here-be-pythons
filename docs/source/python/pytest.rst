.. _python_pytest:

Pytest - Test Framework
=======================

.. admonition:: Main point
   :class: tip

   `Pytest <https://docs.pytest.org/en/latest/>`_ is a programmer-friendly Python test framework. It makes it easy to write small tests, yet scales to support complex cases.


+ Major ``pytest`` features:

    + Battle-tested and mature.

    + Informative test failures.

    + Less verbose (plain ``assert`` vs. ``self.assertEqual``, ``self.assertGreaterEqual``, etc.).

    + Classes are not required.

    + A far more convenient way to write setup & teardown functions with fixtures.

    + Parameterized tests.

    + Fantastic test runner (a.o. marker- and name-based test selection).

    + Rich plugin architecture.

    + Auto-discovery of test modules and functions.

    + Runs ``unittest`` and ``nose`` test suites out-of-the-box.

+ You can easily set test runner default flags by defining them in a configuration file called ``pytest.ini``. You can find an example in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/pytest.ini>`_.

+ Recommended test runner plugins:

    + `pytest-cov <https://pypi.org/project/pytest-cov/>`_ - prints coverage report at the end of test runner report.

    + `pytest-mock <https://pypi.org/project/pytest-mock/>`_ - adds ``mocker`` fixture, which makes mocks easier and more readable.

    + `pytest-socket <https://pypi.org/project/pytest-socket/>`_ - disables socket calls during tests to ensure network calls are prevented. Amazing to protect yourself against incidental DB or API calls.

    + `pytest-sugar <https://pypi.org/project/pytest-sugar/>`_ - makes test runner report even nicer.

+ Useful content:

    + `Official documentation <https://docs.pytest.org/en/latest/contents.html>`_

    + `Python Testing with pytest: Simple, Rapid, Effective, and Scalable <https://www.amazon.com/Python-Testing-pytest-Effective-Scalable/dp/1680502409>`_
