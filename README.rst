How to make our own python packages:
====================================

Initial steps:
--------------
- Download VSCode
    - open up a unique folder and name it
- Determine if you already have the tools. Open up Terminal (main selection at the top of VScode)
    - environmental manager (conda/mamba)
        - Create an environment:

        .. code-block:: bash

            mamba create -n ChevLab_Add python=3.8
            mamba activate ChevLab_Add

        - mamba can be substituted for conda
            - mamba is much faster at resolving packages and environments
        - Install conda with Anaconda or miniconda
            https://conda.io/projects/conda/en/latest/user-guide/install/index.html
            https://docs.conda.io/en/latest/miniconda.html

        - Install mamba with (if you already have conda):

        .. code-block:: bash

            conda install mamba -n base -c conda-forge

        - Otherwise:
            https://github.com/conda-forge/miniforge#mambaforge


Now we need to make sure we all have python/pip etc.
-----------------------------------------------------

- What we’ll need to create, build, package and upload your python package:

.. code-block:: bash

    python --version
    #If no python then install via:
    #https://docs.python-guide.org/starting/installation/#installation
    #pip will be installed with python3 but if not
    python3 -m pip --version

Links:
https://packaging.python.org/en/latest/tutorials/installing-packages/

See "Installing from other Indexes" in above link.

https://packaging.python.org/en/latest/flow/

https://packaging.python.org/en/latest/tutorials/packaging-projects/


Both links have useful information on packaging. Including the following:


""
The first thing you’ll need to do is register an account on TestPyPI, which is a separate instance of the package index intended for testing and experimentation. It’s great for things like this tutorial where we don’t necessarily want to upload to the real index. To register an account, go to https://test.pypi.org/account/register/ and complete the steps on that page. You will also need to verify your email address before you’re able to upload any packages. For more details, see Using TestPyPI.

To securely upload your project, you’ll need a PyPI API token. Create one at https://test.pypi.org/manage/account/#api-tokens, setting the “Scope” to “Entire account”. Don’t close the page until you have copied and saved the token — you won’t see that token again.

Now that you are registered, you can use twine to upload the distribution packages. You’ll need to install Twine:
You will be prompted for a username and password. For the username, use __token__. For the password, use the token value, including the pypi- prefix.
""


.. code-block:: bash

    python3 -m pip install --upgrade build
    python3 -m pip install --upgrade twine


Finally we’re ready to create our package!
--------------------------------------------
Source files needed:

- ChevLab_add/
    - __init__.py
    - main.py
- pyproject.toml
- LICENSE
- README.rst

- tests/
    - test_data/
        - Dataframe.txt
    - main_test.py

.. code-block:: bash

    #In the package repository
    python3 -m build
    python3 -m twine upload --repository testpypi dist/*

Testing your package from test.pypi
------------------------------------

.. code-block:: bash

    #In your environment (not base)
    python -m pip install --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple chevlabpkg

Future things to address
------------------------
Things we can further touch on if of interest in the future:
- Building and uploading the package to pypi (for pip install)
    - Further discussion on pyproject.toml, dependencies, etc.
- Test folder and test scripts using pytest and why they're used
- Github, git version control and commits with a package
- Creating a release on Github
- Github actions to automatically test your packages monthly or for each version you push
    - Helpful if you have dependencies and want to keep ahead of breaks in the code caused by new versions of your dependencies (pandas in this case)
- Creating a conda recipe for uploading to conda channels