.. _git_semantic_commit_messages:

Semantic Commit Messages
========================

.. admonition:: Main point
   :class: tip

   Adding standardized, meaningful prefix to each commit message may significantly improve readability. Also, it facilitates keeping up-to-date CHANGELOG.

+ To begin with, let's start with a few examples of semantic commit messages:

    + ``feat: Notify shopper about successful product shipment``

    + ``tests: Add tests for class <PeriodicPayment>``

    + ``rfct: Refactor Invoke tasks for managing Docker containers``

+ As you can see, semantic commit messages stand for prefixing commit messages in a standardized, meaningful way. In effect:

    + It is easier to read and scan commit messages (be it during Pull Request, or when you are looking for that-one-particular-bugfix).

    + It makes maintaining CHANGELOG (almost) a pleasure. Simply group commit messages in their respective sections, which means putting all ``feat`` commits under ``Features``, all ``rfct`` commits under ``Refactoring``, etc.

        + An exciting idea is to do it in reverse i.e., first add a new row to CHANGELOG, and then use this row to create the commit message. For instance:

          Under section ``Docs`` write a new line:

          ``- Update 'New Machine Configuration' section in README.``

          Then add above change to CHANGELOG to staging and make a commit with the copied message:

          ``docs: Update 'New Machine Configuration' section in README``

+ There is no single standard for semantic commit messages prefixes. And this is fine! You should tailor the rules to fit your project's needs. Still, a nice place to start might be the list below:

    + ``bugs`` = fixes for bugs that are visible for the users

    + ``depl`` = deployment scripts, Docker configs, etc.

    + ``docs`` = changes to the documentation

    + ``feat`` = new feature for the users

    + ``front`` = frontend changes

    + ``misc`` = miscellaneous i.e. any other business

    + ``perf`` = performance improvements

    + ``rfct`` = refactoring

    + ``style`` = code formatting

    + ``tests`` = adding new tests, refactoring existing tests

    + ``ver`` = new release

+ You can educate yourself further by reading how others implement the grand idea of semantic commit messages:

    + `joshbuchea's gist <https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716>`_

    + `Conventional Commits website <https://www.conventionalcommits.org>`_
