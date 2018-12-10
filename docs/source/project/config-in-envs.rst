.. _project_config_in_envs:

Store config in ENVs
====================

.. admonition:: Main point
   :class: tip

   The `Twelve-Factor App <https://12factor.net/config>`_ stores config in the environment variables.


+ This definition of 'config' does not include internal application controls, such as Django or Flask knobs & flags. This type of settings does not vary between deploys, nor contains sensitive credentials, so is best done in the code.

+ **A litmus test for whether an app has its config correctly factored out of the code is whether the codebase could be made open source at any moment without compromising any secrets or credentials.**

+ Usually there are multiple ENV files e.g. a separate version for development, staging and production.

    + It is convenient to organise those ENVs in one location. An example of such organisation is present in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/tree/master/%7B%7Bcookiecutter.project_dir%7D%7D/envs>`_. As a bonus, you can find there Python ENVs loader based on `python-dotenv <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/envs/loader.py>`_.
