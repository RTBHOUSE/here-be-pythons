.. _project_ci:

Continuous Integration - Kill Bugs Fast
=======================================

Volumes have been written about `Continuous Integration <https://docs.microsoft.com/en-us/azure/devops/learn/what-is-continuous-integration>`_ (along with Continuous Delivery and Deployment), yet...

.. admonition:: Main point
   :class: tip

    `The absolute minimum every project absolutely positively <https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/>`_ must implement is to verify each check-in to a hosted/shared version control by an automated tool. All in order to detect problems early.


+ Keeping it more serious, CI will take a lot of mental burden off your head. You cannot assume that every contributor has correctly configured Pre-commit Git Hook. You cannot assume everyone will remember to test and lint. You cannot even trust yourself, because sooner or later you will also make some stupid mistake. That is why you hire CI - to always have your project's back. (Sometimes even for free!)

+ There are numerous CI tools, both closely related to your hosting services (like Bitbucket Pipelines or GitLab CI/CD) as well as platform-independent ones (like Jenkins or Circle CI). Choose whatever floats your boat.

+ **As to what to check during CI, at least run the tests to double-check they pass.** A handful of other ideas:

    + Iron the new code with your linters of choice.

    + Test if the project still builds correctly.
