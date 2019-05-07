.. _project_logging:

Logging Is a Programmer's Best Friend
=====================================

.. admonition:: Main point
   :class: tip

   You should log. No excuses.


+ Logging makes the flow of the application obvious & visible. This helps every interested party to reason about what and when is happening.

+ If done right, logging may literally save your day when real problems shred your beautiful code to pieces (especially in the 🔥production environment🔥, where debugging turns into a literal nightmare).

+ It can be tedious to configure the logging yourself. That is why in `Big-Bang-py <https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/%7B%7Bcookiecutter.project_source_code_dir%7D%7D/logging_config.py>`_ you can find pre-configured setup that is ready-to-go.

    + In proposed setup logs are streamed to stderr as well as saved in ``$PROJECT_ROOT/logs``.

    + Logs saved on the drive are processed by `RotatingFileHandler <https://docs.python.org/3/library/logging.handlers.html#rotatingfilehandler>`_. Therefore there is no risk that log files will grow indefinitely.

    + How to get started?

      .. code-block:: python

         # Load logging config
         import logging.config
         from src.logging_config import DICT_CONFIG
         logging.config.dictConfig(DICT_CONFIG)

         # Get logger
         logger = logging.getLogger('main')

         # Logging time!
         logger.info('* THE GREAT BIRD IS LISTENING *')


.. admonition:: Power-Hint!
   :class: tip

    ``Flake8 + Pipfile`` configuration of Big-Bang-py repo uses `flake8-print plugin <https://github.com/JBKahn/flake8-print>`_, which will find and warn you about using print statements. If they are no longer necessary, remove them. But if they are... log there! There is great chance that sooner or later you will need this information again.

+ You can learn more about logging basics on `Real Python <https://realpython.com/python-logging/>`_.

    + If you are an adventurous programmer with no faint-heart, there is `the official Python logging documentation <https://docs.python.org/3/library/logging.html>`_ waiting out there. Bear in mind that because of this document, and its unnecessary complexity, a lot of people were scared off and have been using prints ever since.
