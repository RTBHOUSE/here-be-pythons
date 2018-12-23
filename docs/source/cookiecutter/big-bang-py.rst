.. _cookiecutter_big_bang_py:

Big-Bang-py
===========

To start your new Python project, it is recommended to use `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py>`_ Cookiecutter, as it follows the ideas and principles of Here-Be-Pythons!

Moreover, it is maintained by the very same authors 😊, so both projects are promised to be kept in sync 💫.


Usage
-----

.. code-block:: console

    # Generate a new project.
    > cookiecutter gh:RTBHOUSE/big-bang-py

    # Answer all of the prompted questions.
    # Brackets show default options. Click <enter> if you wish to accept them.
    project_name [My New Project]: ???
    project_dir  [my-new-project]: ???
    project_source_code_dir [src]: ???

    # Finish with:
    > cd $MY_NEW_PROJECT_DIR
    > ./finish_project_setup
    > ./invoke_bash_completion \
          && rm -f invoke_bash_completion \
          && source $VIRTUAL_ENV/bin/activate

And voilà! You are ready to code!
