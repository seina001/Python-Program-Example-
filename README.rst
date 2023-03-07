How to make our own python packages:
====================================

GUI compiler and tools needed:
------------------------------
First we'll need Visual Studio Code, which wraps useful plugins like git, jupyter, docker, terminal, 
and also has a good realtime graphical representation of function descriptions, problems and debugging.

- Download VSCode:
    - https://code.visualstudio.com/download
    - craete a unique folder and name it

Now that we have a folder open, lets create an environment for us to work in using mamba or conda:

- Determine if you already have the tools. Open up Terminal (main selection at the top of VScode)
    - environmental manager (conda/mamba)
        - Create an environment:

        .. code-block:: bash

            #you should see "(base)" at the start of your terminal line
            mamba create -n ChevLab_Add python=3.8
            #mamba create (creating a "sandbox" to work in), -n naming it CHevLab_Add, with python=3.8 installed with it's dependencies
            mamba activate ChevLab_Add
            #activate this environment

        - mamba can be substituted for conda

            - mamba is much faster at resolving packages and environments

        - Install conda with Anaconda or miniconda

            - https://conda.io/projects/conda/en/latest/user-guide/install/index.html
            - https://docs.conda.io/en/latest/miniconda.html

        - Install mamba with (**if you already have conda**):

        .. code-block:: bash

            conda install mamba -n base -c conda-forge

        - Otherwise, install it following this link:

            - https://github.com/conda-forge/miniforge#mambaforge
            - Follow the instructions and install your compatible file for "Mambaforge". This installs Mamba in the base environment.


Now we need to make sure we all have python/pip etc.
-----------------------------------------------------

What we’ll need to create, build, package and upload your python package:

.. code-block:: bash

    python --version
    #If no python then install via:
    #https://docs.python-guide.org/starting/installation/#installation
    #pip will be installed with python3 but if not
    python3 -m pip --version


Additional information on python packaging:

    - https://packaging.python.org/en/latest/tutorials/installing-packages/
    - See "Installing from other Indexes" in above link.

Additional information on files necessary to build your python package:

- https://packaging.python.org/en/latest/flow/
- https://packaging.python.org/en/latest/tutorials/packaging-projects/


Both links have useful information on packaging. Including the following to test your package by uploading to test.pypi:


""
The first thing you’ll need to do is register an account on TestPyPI, which is a separate instance of the package index intended for testing and experimentation. It’s great for things like this tutorial where we don’t necessarily want to upload to the real index. To register an account, go to https://test.pypi.org/account/register/ and complete the steps on that page. You will also need to verify your email address before you’re able to upload any packages. For more details, see Using TestPyPI.

To securely upload your project, you’ll need a PyPI API token. Create one at https://test.pypi.org/manage/account/#api-tokens, setting the “Scope” to “Entire account”. Don’t close the page until you have copied and saved the token — you won’t see that token again.

Now that you are registered, you can use twine to upload the distribution packages. You’ll need to install Twine:
You will be prompted for a username and password. For the username, use __token__. For the password, use the token value, including the pypi- prefix.
""


We'll also need the tools to build and upload our package (build and twine):

.. code-block:: bash

    python3 -m pip install --upgrade build
    python3 -m pip install --upgrade twine


Finally we’re ready to create our package!
--------------------------------------------
Source files needed:

.. code-block:: bash

    mypackage/          #Folder that your package is called
        __init__.py     #Package initializer, tells your computer which files it needs to run your package
        main.py         #Main program file
    pyproject.toml      #Package setup file, is used to build your package and install dependencies etc. (setup.py/setup.cfg is depreciated)
    LICENSE             #Licensing file
    README.rst          #Readme file, formatted for Github repository
    tests/              #Test folder, used to run pytest to test individual functions
        test_data/      #Test data folder
            Dataframe.txt    #Test data file
        main_test.py    #Test script, running asserts/error messaging confirmations to determine our program is running as it should


Let's now build our python package by building our distribution files (tar.gz/wheel files) and uploading to test.pypi:


.. code-block:: bash

    #In the package repository
    python3 -m build
    python3 -m twine upload --repository testpypi dist/*


Testing your package from test.pypi
------------------------------------

.. code-block:: bash

    #In your environment (not base), --index-url refers to your package host (test.pypi), --extra-index-url refers to another package host for your dependencies (pandas)
    python -m pip install --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple mypackage



Future things to address
------------------------

Things we can further touch on if of interest in the future:

- Building and uploading the package to pypi (for pip install)
    - Further discussion on pyproject.toml, dependencies, etc. and 
- Test folder and test scripts using pytest and why they're used
- Github, git version control and commits with a package
- Creating a release on Github
- Github actions to automatically test your packages monthly or for each version you push
    - Helpful if you have dependencies and want to keep ahead of breaks in the code caused by new versions of your dependencies (pandas in this case)
- Creating a conda recipe for uploading to conda channels