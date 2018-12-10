import invoke


@invoke.task
def build_docs(c):
    """Build Sphinx HTML docs. """
    c.run('sphinx-build -E -a -b html docs/source/ docs/build/html/')


@invoke.task
def develop_docs(c):
    """
    Open Sphinx HTML docs in the browser with hot reloading.

    The browser opens after 2 seconds.
    """
    c.run('sphinx-autobuild -b html --open-browser --delay 2 docs/source/ docs/build/html/')


################################
# Organise Invoke's namespaces #
################################

# The main namespace MUST be named `namespace` or `ns`.
# See: http://docs.pyinvoke.org/en/1.2/concepts/namespaces.html
namespace = invoke.Collection()

docs_namespace = invoke.Collection('docs')
docs_namespace.add_task(build_docs, 'build')
docs_namespace.add_task(develop_docs, 'develop')
namespace.add_collection(docs_namespace)
