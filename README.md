# Here-Be-Pythons!

+ Here-Be-Pythons!™ holds opinionated best practices & ideas to help you build your next Python project.

+ The goal is to gather the sweetest & most impactful nuggets of Python projects wisdom and make them accessible from a single place. 

+ Hopefully, Here-Be-Pythons! will inspire you to code your awesome projects faster and to make them even better.

#### Warning! Opinions ahead!

+ The content of this repo is based on the research, experience, but also pure opinions of the authors. And opinions do differ! However, we are more than happy to hear your feedback to improve this repo and grow as programmers.


## TL;DR Checklist

+ Python:

    + Use [Python 3.7](https://docs.python.org/3/whatsnew/3.7.html).
    
    + Manage app dependencies using [Pipenv](https://pipenv.readthedocs.io/en/latest).
    
    + Sort imports with [Isort](https://github.com/timothycrosley/isort).
    
    + Format source files with [YAPF](https://github.com/google/yapf).
    
    + Lint code with [Flake8](https://github.com/PyCQA/flake8).
    
    + Use [pytest](https://docs.pytest.org/en/latest/) as test framework.

+ Git:

    + Use [.gitignore](https://git-scm.com/docs/gitignore).
    
    + Use [pre-commit Git hook](https://githooks.com).

+ Project:

    + Store config (credentials, secrets, etc.) in [the environment](https://12factor.net/config).
    
    + Manage and execute command line tasks via [Invoke](http://www.pyinvoke.org).
    
    + [Log, log, log.](https://realpython.com/python-logging/)
    
    + Maintain up-to-date [README](https://www.makeareadme.com).
    
    + Set up [Continuous Integration](https://docs.microsoft.com/en-us/azure/devops/learn/what-is-continuous-integration).


## Table of Contents

#### Cookiecutter

* [Big-Bang-py - Cookiecutter for Python projects](#big-bang-py---cookiecutter-for-python-projects)

#### Python

* [Python version](#python-version)
* [Pipenv - App Package Manager](#pipenv---app-package-manager)
* [Isort - Imports Sorter](#isort---imports-sorter)
* [YAPF - Files Formatter](#yapf---files-formatter)
* [Flake8 - Octo-Ninja Linter](#flake8---octo-ninja-linter)
* [McCabe - Code Complexity Checker](#mccabe---code-complexity-checker)
* [Pytest - Test Framework](#pytest---test-framework)

#### Git

* [.gitignore](#gitignore)
* [Pre-commit Git Hook](#pre-commit-git-hook)

#### Project

* [Store config in ENVs](#store-config-in-envs)
* [Invoke - Manage & Execute Tasks](#invoke---manage--execute-tasks)
* [Logging Is A Programmer's Best Friend](#logging-is-a-programmers-best-friend)
* [README - Gateway to Your Code](#readme---gateway-to-your-code)
* [Continuous Integration - Kill Bugs Fast](#continuous-integration---kill-bugs-fast)


## Big-Bang-py - Cookiecutter for Python projects

+ To start your new Python project, it is recommended to use [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py) Cookiecutter. It follows the ideas and principles of Here-Be-Pythons! Moreover, it is maintained by the very same authors :blush:, so both repos will be kept in sync :dizzy:
    

## Python version

+ **It is recommended to use Python 3.7.**

+ There is an informative summary of new features on [Real Python](https://realpython.com/python37-new-features). More detailed description can be found in [the official documentation](https://docs.python.org/3/whatsnew/3.7.html).

+ To name some notable additions:

    + [Data Classes](https://realpython.com/python-data-classes) can easily replace [namedtuples](https://docs.python.org/3.7/library/collections.html#collections.namedtuple) and [attrs](https://github.com/python-attrs/attrs).
    
    + [Typing Forward Reference](https://realpython.com/python37-new-features/#typing-enhancements) makes type hints even more programmer-friendly.

    + The `asyncio` module has received many [new features along with usability and performance improvements](https://tryexceptpass.org/article/asyncio-in-37/). For instance,  new `asyncio.run()` automatically creates an event loop, runs a task on it and finally closes the loop when the task is done.
    
+ Nonetheless, if you still use previous version of Python (especially 3.6), it is possible to backport some of the new features e.g. [Data Classes](https://github.com/ericvsmith/dataclasses).


## Pipenv - App Package Manager

+ **Use [Pipenv](https://pipenv.readthedocs.io/en/latest) to manage Python [app dependencies](https://pipenv.readthedocs.io/en/latest/advanced/#pipfile-vs-setup-py).**
  
+ Pipenv consolidates `pip` & `virtualenv` while offering powerful new features. Among others:

    + Virtual environment is created and managed automatically.
    
    + Project dependencies are installed using `Pipfile` (building from the latest allowed versions of packages) or `Pipfile.lock` (making build deterministic):
    
        + `Pipfile` specifies only the packages you need, as those are abstract dependency declarations. Sub-dependencies are taken care of by Pipenv.
        
        + `Pipfile.lock` uses hashes to lock all of the dependencies (including sub-dependencies). This ensures repeatable, deterministic builds. You never manage this file by hand, leaving the matter for Pipenv.
   
+ Essential commands:

    + `install` - installs provided packages and adds them to Pipfile. If no packages are given, installs all packages from `Pipfile`.

    + `sync` - deterministic build! Installs all packages specified in `Pipfile.lock`.
    
    + `shell` - spawns a shell with the virtualenv activated.
    
        + [Shell environment will be automatically updated with ENVs from `.env` file](https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-automatic-loading-of-env).
    
    + `run` - runs a given command from the virtualenv with forwarded arguments.
    
        + [Shell environment will be automatically updated with ENVs from `.env` file](https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-automatic-loading-of-env).
    
    + `graph` - shows a dependency graph of the installed dependencies.
    
    + `check` - most importantly, checks for security vulnerabilities.

+ You can educate yourself further by reading [Real Python's guide](https://realpython.com/pipenv-guide). It is also recommended to go through [the official documentation](https://pipenv.readthedocs.io/en/latest/#further-documentation-guides).

+ **An example of Pipfile might be found in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/tree/master/%7B%7Bcookiecutter.project_dir%7D%7D/Pipfile).**


## Isort - Imports Sorter

+ **[Isort](https://github.com/timothycrosley/isort) automatically sorts and groups Python imports.**

+ There are several knobs configuring Isort's behavior. Full reference of settings can be found [here](https://github.com/timothycrosley/isort/wiki/isort-Settings#full-reference-of-isort-settings).

+ You can specify project level configuration by placing `.isort.cfg` file at the root of your project.

    + You may find pre-configured `.isort.cfg` in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/.isort.cfg).
    
+ It is recommended to include Isort in your linting Invoke task and also to run it during pre-commit Git hook. Example of both can be found in Big-Bang-py, see [tasks.py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks.py#L41-L46) and [pre-commit](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/hooks/pre-commit#L36-L45).

+ To manage edge cases, [disable Isort per line or for entire file](https://github.com/timothycrosley/isort#skip-processing-of-imports-outside-of-configuration).


## YAPF - Files Formatter

+ **[YAPF](https://github.com/google/yapf) is a Python files formatter. Its goal is to make the code look as good as written by a programmer who is rigorously following a style guide.**

+ The formatting style used by YAPF is configurable, where specific configuration can be pointed in a couple of ways.

    + It is recommended to store the configuration in a properly formatted `.style.yapf` file at the root of your project.

    + You may find pre-configured `.style.yapf` in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/.style.yapf).

+ It is recommended to include YAPF in your linting Invoke task and also to run it during pre-commit Git hook. Example of both can be found in Big-Bang-py, see [tasks.py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks.py#L48-L52) and [pre-commit](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/hooks/pre-commit#L47-L59).

+ Survival tips:
    
    + If you leave trailing comma in a collection (list, function parameters, etc.), YAPF will force the collection to break, giving one element per line.
    
    + From time to time you WILL see weirdly formatted code, as YAPF is not perfect. There are at least two major occurrences:
 
        + Deeply Nested Dicts - this is quite understandable as decisions that improve readability are usually arbitrary and should be solved on a case-by-case basis.
         
        + Complex Comprehensions - comprehensions are split over multiple lines only when they exceed the column limit... This issue is brought to the attention of both YAPF authors (see issue on [Github](https://github.com/google/yapf/issues/628)) and other programmers (see posts on [Reddit](https://www.reddit.com/r/Python/comments/9mov4r/is_there_a_way_to_force_yapf_to_always_splitfold) and [Stack Overflow](https://stackoverflow.com/questions/52558919/is-there-a-way-to-force-yapf-to-always-split-fold-comprehensions)).
  
    + To manage edge cases, [disable YAPF per line or per block](https://github.com/google/yapf#why-does-yapf-destroy-my-awesome-formatting). 


## Flake8 - Octo-Ninja Linter

+ [Flake8](https://github.com/PyCQA/flake8) is a wrapper around three tools:

    1. [PyFlakes](https://github.com/PyCQA/pyflakes) - **checks for Python errors.**
    
    1. [pycodestyle](https://github.com/PyCQA/pycodestyle) - **tests Python code against some of the style conventions in [PEP 8](https://www.python.org/dev/peps/pep-0008/).**
    
    1. [McCabe](https://github.com/PyCQA/mccabe) - **analyses Python code complexity** (see the [next section](#mccabe---code-complexity-checker) for more details).

+ Flake8 combines so much linter-power under the hood of a single tool. If used correctly, it will make your code not only more consistent, but simply better (and more pythonic :snake:).

+ Flake8 is configurable, where specific setup can be pointed in a [couple of ways](http://flake8.pycqa.org/en/latest/user/configuration.html).

    + You may find pre-configured .flake8 in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/.flake8).

+ There is an abundance of [plugins](http://flake8.pycqa.org/en/latest/user/using-plugins.html) greatly extending capability of Flake8 - search for them on GitHub.

    + A bunch of plugins are included in Flake8 configuration of Big-Bang-py. See all `flake8-*` packages in [Pipfile](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/Pipfile#L12-L17).
    
    + An interesting example is [flake8-html](https://github.com/lordmauve/flake8-html), which generates readable Flake8 HTML report (works similar to `coverage html`).

+ It is recommended to include Flake8 in your linting Invoke task and also to run it during pre-commit Git hook. Example of both can be found in Big-Bang-py, see [tasks.py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks.py#L54-L58) and [pre-commit](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/hooks/pre-commit#L61-L77).


## McCabe - Code Complexity Checker

+ [mccabe](https://github.com/pycqa/mccabe) library automatically detects over-complex code basing on cyclomatic complexity.
 
+ Cyclomatic complexity is approximately equivalent to one plus the number of loops and if statements. The simple interpretation is that it shows an upper bound for the number of test cases required to obtain branch coverage of the code, therefore it roughly indicates the effort required for writing tests.

    + Additional explanations can be found on [tutorialspoint](https://www.tutorialspoint.com/software_testing_dictionary/cyclomatic_complexity.htm) and [Wikipedia](https://en.wikipedia.org/wiki/Cyclomatic_complexity).

+ Code with high cyclomatic complexity (usually assumed as 10+) is likely to be difficult to understand and therefore have a higher probability of containing defects.
    
+ It is recommended to include McCabe in your linting Invoke task and also to run it during pre-commit Git hook. In Big-Bang-py McCabe is run automatically by Flake8 linter.

    + Cut-off complexity in Invoke task and pre-commit is arbitrarily assumed to be 7 (configured by [max-complexity](http://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-max-complexity) set in [.flake8](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/.flake8#L43-L44)). However, this number should be adjusted to reflect your experience and project needs.


## Pytest - Test Framework

+ **[Pytest](https://docs.pytest.org/en/latest/) is programmer-friendly Python test framework. It makes it easy to write small tests, yet scales to support complex cases.**

+ Major features:

    + Battle-tested and mature.
    
    + Informative test failures.
    
    + Less verbose (plain `assert` vs. `self.assertEqual`, `self.assertGreaterEqual`, etc.)
     
    + Classes are not required.
     
    + A far more convenient way to write setup & teardown functions with fixtures.
     
    + Parameterized tests.
     
    + Fantastic test runner (a.o. marker- and name-based test selection).
    
    + Rich plugin architecture.
    
    + Auto-discovery of test modules and functions.
    
    + Can run unittest and nose test suites out of the box.
    
+ You can easily set test runner default flags by defining them in a configuration file called `pytest.ini`. You can find an example in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/pytest.ini).

+ Recommended test runner plugins:

    + [pytest-cov](https://pypi.org/project/pytest-cov/) - prints coverage report at the end of test runner report.
    
    + [pytest-mock](https://pypi.org/project/pytest-mock/) - adds `mocker` fixture, which makes mocks easier and more readable.

    + [pytest-socket](https://pypi.org/project/pytest-socket/) - disables socket calls during tests to ensure network calls are prevented. Amazing to protect yourself against incidental DB or API calls.

    + [pytest-sugar](https://pypi.org/project/pytest-sugar/) - makes test runner report even nicer.

+ Useful content:

    + [Why pytest?](http://thesoftjaguar.com/pres_pytest.html#/)
    
    + [Official documentation](https://docs.pytest.org/en/latest/contents.html)
    
    + [Python Testing with pytest: Simple, Rapid, Effective, and Scalable](https://www.amazon.com/Python-Testing-pytest-Effective-Scalable/dp/1680502409)
 

## .gitignore

+ **ALWAYS use [.gitignore](https://git-scm.com/docs/gitignore). It specifies files intentionally ignored by Git.**

+ If you are using PyCharm, definitely install [.ignore plugin](https://github.com/hsz/idea-gitignore). This will make managing `.gitignore` a breeze. 

+ Alternatively, it is possible to generate .gitignore online using [gitignore.io](https://www.gitignore.io).

+ You may also find an example of `.gitignore` for Python project in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/.gitignore).


## Pre-commit Git Hook

+ **The pre-commit [Git hook](https://githooks.com) is run before you even start typing new commit message.**

+ It is a perfect opportunity to automatically run tests and linters, so your code stays consistent and readable, while working as intended.

+ You can find an example of pre-commit Git hook in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/hooks/pre-commit).

    + `install_precommit` Invoke task in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks.py#L27-L35) takes your pre-commit Git Hook from `/hooks/pre-commit` and automatically sets it up for you.


## Store config in ENVs

+ **The [Twelve-Factor App](https://12factor.net/config) stores config in environment variables.**

    + Note that this definition of 'config' does not include internal application config, such as Django or Flask knobs & settings. This type of config does not vary between deploys, nor contains sensitive credentials, so is best done in the code.

+ **A litmus test for whether an app has its config correctly factored out of the code is whether the codebase could be made open source at any moment without compromising any secrets or credentials.**

+ Usually there are multiple ENV files, for instance separate versions for testing, development and production.

    + It is convenient to organise those ENVs in one location. An example of such organisation is present in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/tree/master/%7B%7Bcookiecutter.project_dir%7D%7D/envs). As a bonus, you can find there Python ENVs loader based on [python-dotenv](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/envs/loader.py).


## Invoke - Manage & Execute Tasks

+ **Turn into a task every project related shell command which will be called more than a couple of times and is not super-common** (like `ls` with basic flags).

+ **Manage and execute those project tasks via [Invoke](http://www.pyinvoke.org).**

+ You can replace `Makefiles` and similar straightaway, as Invoke is dead simple.

+ Invoke tasks are called by typing in the shell `invoke *task-name*`

+ Invoke tasks are normal Python functions organised in `tasks.py` file.

+ Docstrings of functions implementing Invoke tasks are automatically formatted into a command line help:

```
>>> invoke --list
Available tasks:

  task1   First line of task1 docstring.
  task2   First line of task2 docstring.

>>> invoke --help task2
Usage: inv[oke] [--core-opts] task2 [--options] [other tasks here ...]

Docstring:
  Full docstring of task 2.

Options:
  -p TYPE, --param=TYPE   Your additional parameters help string. 
                          See: http://docs.pyinvoke.org/en/0.11.0/getting_started.html#adding-help-for-parameters.
```

+ [Invoke tasks can be organised using namespaces](http://docs.pyinvoke.org/en/1.2/getting-started.html#creating-namespaces). Then, for instance, you can call server tasks like `jenkins.deploy`/`jenkins.logs` or organise job-related tasks like `job.start`/`job.stop`.

+ Invoke can be easily buffed with [shell tab completion](http://docs.pyinvoke.org/en/1.2/invoke.html#shell-tab-completion).

    + If you work on your projects using `bash` with virtualenv created by `pipenv shell`, a ready-2-go installation script can be found in the file `invoke_bash_completion` in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/invoke_bash_completion). If your development environment differs, this script can still give you a basis, or at least a hint, how to build a solution of your own. 

+ You may find examples of Invoke tasks in the `tasks.py` in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/tasks.py).

+ [The official documentation](http://docs.pyinvoke.org/en/1.2/) is solid. Get familiar with it.


## Logging Is A Programmer's Best Friend

+ **You should [log](https://realpython.com/python-logging/). No excuses.**

+ Logging makes the flow of the application obvious & visible. This helps every interested party to reason about what and when is happening.

+ If done right, logging may literally save your day when real problems shred your beautiful code to pieces in production environment.

+ It can be tedious to configure the logging yourself. That is why in [Big-Bang-py](https://github.com/RTBHOUSE/big-bang-py/blob/master/%7B%7Bcookiecutter.project_dir%7D%7D/%7B%7Bcookiecutter.project_source_code_dir%7D%7D/logging_config.py) you can find pre-configured setup that is ready-to-go.

    + In proposed setup logs are streamed to stderr as well as saved in `$PROJECT_ROOT/logs`.

    + Logs saved on the drive are processed by [RotatingFileHandler](https://docs.python.org/3/library/logging.handlers.html#rotatingfilehandler). Therefore there is no risk that log files will grow indefinitely.

    + How to log:
    
        ```python
        # Load logging config
        import logging.config
        from src.logging_config import DICT_CONFIG
        logging.config.dictConfig(DICT_CONFIG)
        
        # Get logger
        logger = logging.getLogger('main')
        
        # Logging time!
        logger.info('* THE GREAT BIRD IS LISTENING *')
        ```
+ **Power-Hint:** `Flake8 + Pipfile` configuration of Big-Bang-py repo uses [flake8-print plugin](https://github.com/JBKahn/flake8-print), which will **find and warn you about using print statements. If they are no longer necessary, remove them. But if they are... log there! There is great chance that sooner or later you will need this information again.**

+ Learn more about logging in a digestible form on [Real Python](https://realpython.com/python-logging/). 

    + If you are an adventurous programmer that knows no fear, there is [the official documentation](https://docs.python.org/3/library/logging.html) waiting out there. Bear in mind that because of this document, and its unnecessary complexity, a lot of people were scared off and have been using prints ever since.


## README - Gateway to Your Code

+ **Make a README. Because no one can read your mind ([yet](https://www.makeareadme.com/#mind-reading) :grinning:).**

+ **By bringing the most essential knowledge about the project in a structured manner, README serves as a lantern for all of the programmers from the future. Including the future you!**

    + To expand a bit, we should be honest and accept that over time code becomes more and more alien. To put it in a more poetic way, [legacy code is anything we’re not writing right now](https://itnext.io/it-doesnt-have-to-be-perfect-25071b56959b). And without a solid startup documentation it will be super easy to get lost with a very grim perspective to get found.

+ There is no obvious consensus regarding what README should contain. However, it seems that a good one should answer at least:

    + What is the project about?
        
    + Why is it needed?
        
    + How does it solve the problem?
    
    + How to install & build the source code?
    
        + Including how to check if the code works as intended? (e.g. How to run the tests?)
    
    + How to use the application?
    
    + How to deploy?
    
    + How to contribute?
    
+ If you want to get inspired, [Make a README](https://www.makeareadme.com/) and [Awesome README](https://github.com/matiassingers/awesome-readme#articles) are fantastic places to dig.

+ The recommended format of README is [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). It is simple, powerful and popular, making it a perfect choice for most of the projects.


## Continuous Integration - Kill Bugs Fast

+ Volumes have been written about Continuous Integration (along with Continuous Delivery and Deployment). Yet the absolute minimum every project absolutely positively must implement is to **verify each check-in to a hosted/shared version control by an automated tool in order to detect problems early.**

+ **In the short, medium and long-term CI will save you tons of blood & tears. You will also sleep better at night.**

    + Keeping it more serious, CI will take a lot of mental burden off your head. You cannot assume that every contributor has correctly configured pre-commit Git hook. You cannot assume everyone will remember to test and lint. You cannot even trust yourself, because sooner or later you will also make some stupid mistake. That is why you hire CI - to have your project's back.

+ There are numerous CI tools, both closely related to your hosting service (like Bitbucket Pipelines or GitLab CI/CD) as well as platform-independent ones (like Jenkins or Circle CI). Choose whatever floats your boat.

+ **As to what to check during CI, at least run the tests to double-check they pass.** Some other ideas:

    + Iron the new code with your linters of choice.
    
    + Test if the project still builds correctly.
