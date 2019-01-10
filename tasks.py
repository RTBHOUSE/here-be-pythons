import invoke

from utils import cowsay

##############
# Core Tasks #
##############


@invoke.task
def coverage_report(c):
    """Open refreshed coverage report in a browser."""
    c.run('coverage html && open htmlcov/index.html', pty=True)


@invoke.task
def flake8_report(c):
    """Open refreshed Flake8 report in a browser."""
    c.run(
        'python -m flake8 --format=html --htmldir=flake-report; '
        'open flake-report/index.html',
        pty=True
    )


@invoke.task
def linters(c):
    """Lint source code using Isort, YAPF and Flake8 (with various plugins)."""
    print(cowsay('Sort Python imports with Isort'))  # noqa: T001
    c.run('python -m isort --apply --quiet', pty=True)

    print(cowsay('Enforce Python style guide with YAPF'))  # noqa: T001
    c.run('python -m yapf --in-place --recursive .', pty=True)

    print(cowsay('Apply dozens of linters with Flake8'), end='\n\n')  # noqa: T001
    c.run('python -m flake8', pty=True)


@invoke.task
def set_precommit(c):
    """Set pre-commit Git hook saved in `$PROJECT_ROOT/githooks/pre-commit`."""
    c.run(
        'cp githooks/pre-commit .git/hooks/pre-commit '
        '&& chmod +x .git/hooks/pre-commit'
        '&& git config --bool flake8.strict true',
        pty=True
    )


@invoke.task
def tests(c):
    """Run pytests with coverage report."""
    c.run('python -m pytest --cov=find_broken_links --cov-branch', pty=True)


#################
# Building Docs #
#################


@invoke.task
def build_docs(c):
    """Build Sphinx HTML docs and save them in `$PROJECT_ROOT/docs/build/html/`."""
    c.run('sphinx-build -E -a -b html docs/source/ docs/build/html/')


@invoke.task
def develop_docs(c):
    """
    Build Sphinx HTML docs and open them in the browser with hot reloading.

    The browser opens after 2 seconds.
    """
    c.run('sphinx-autobuild -b html --open-browser --delay 2 docs/source/ docs/build/html/')


################################
# Organise Invoke's namespaces #
################################

# The main namespace MUST be named `namespace` or `ns`.
# See: http://docs.pyinvoke.org/en/1.2/concepts/namespaces.html
namespace = invoke.Collection()

namespace.add_task(coverage_report)
namespace.add_task(flake8_report)
namespace.add_task(linters)
namespace.add_task(set_precommit)
namespace.add_task(tests)

docs_namespace = invoke.Collection('docs')
docs_namespace.add_task(build_docs, 'build')
docs_namespace.add_task(develop_docs, 'develop')
namespace.add_collection(docs_namespace)
