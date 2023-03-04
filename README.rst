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

