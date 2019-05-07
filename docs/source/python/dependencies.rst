.. _python_pipenv:

Dependencies Management
=======================

.. admonition:: Main point
   :class: tip

   Use a combo of `virtualenv <https://virtualenv.pypa.io/en/latest/>`_ and `pip-tools <https://github.com/jazzband/pip-tools>`_ to manage Python app dependencies.


There are two general approaches to Python app dependencies management:

1. Use a classic combination of `virtualenv + requirements <https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>`_.

2. Use some "fancy" new tool like `Pipenv <https://docs.pipenv.org/en/latest/>`_ or `Poetry <https://poetry.eustace.io/>`_.

If we go with option number 1, we will miss some truly powerful features, such as:

+ clean & simple approach to deterministic, hash-based builds;

+ easy management of multi-tier dependencies (like ``base``, ``dev``, ``tests``, ``prod`` split);

+ clear separation of main dependencies from sub-dependecies.

On the other hand, new alternatives are usually very bloated, slow and extremely opinionated.

That is why a fusion of `virtualenv <https://virtualenv.pypa.io/en/latest/>`_ and `pip-tools <https://pipenv.readthedocs.io/en/latest/advanced/#pipfile-vs-setup-py>`_ is so powerful. It seems to offer the best of two worlds:

+ It is fast.

+ It is based on good, old virtualenv.

+ It is based on good, old requirements... with a twist! We put the actual dependencies in ``requirements.in`` and pip-tools compiles actual dependencies with all sub-dependencies into their locked, hashed versions in ``requirements.txt``.

  In result, we have simple to manage, hash-based, deterministic builds. Nice!

So give it a try. The sooner you start, the sooner you will fall in love with it 💚


Proposed workflow
-----------------

.. code-block:: shell

   > cd $PYTHON_PROJECT_DIR

   # Below approach seems to be the simplest and the most effective way to handle virtualenvs.
   # 1. It doesn't clutter your filesystem.
   # 2. You always know the location and the name of the environment.
   # 3. PyCharm happily finds the virtualenv as soon as you open the project.
   # 4. It just works. No need for virtualenvwrappers, burritos, Bash aliases, etc.
   > virtualenv venv

   > source venv/bin/activate

   # Don't you dare using pip-tools from the root Python environment!
   # Always use the version from the virtualenv that is locked in your main dependencies file.
   # See: https://github.com/jazzband/pip-tools/issues/328#issuecomment-346685547
   > pip install pip-tools

   # Assumption for the next steps:
   # You have already prepared dependencies files base.in and dev.in in ./requirements/abstract
   > pip-compile \
       --generate-hashes \
       --output-file \
       requirements/locked/base.txt \
       requirements/abstract/base.in
   > pip-compile \
       --generate-hashes \
       --output-file \
       requirements/locked/dev.txt \
       requirements/abstract/dev.in
   > pip-sync requirements/locked/dev.txt
   # You can handle the above shell commands via Invoke tasks.
   # See an example: https://git.io/fjcZ6

+ `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py>`_ is based on the above workflow.

+ Remember that both abstract and locked dependencies should be checked in the Git repository.

+ If you want to have a deterministic build (e.g. in Docker container), Python app dependencies are installed as simple as:

  .. code-block:: shell

     pip install -r requirements/locked/*YOUR_REQUIREMENTS_FILE*.txt
