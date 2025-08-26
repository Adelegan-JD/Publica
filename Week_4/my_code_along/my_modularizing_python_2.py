# IMPORTING MODULES

# 1. Modules can be imported as a whole
import math
# Putting it to use
print(math.sqrt(64))

# 2. Importing as an alias
import math as d
# putting it to use
print(d.pow(5, 3))
# The code above shortens the module's name, and this is commonly used when working with common libraries like numpy, pandas, sci-kit learn, itc

# 3. Importing specific functions or variables
from math import sqrt, pi

print(sqrt(144))
print(pi)
# In the code above, the prefix math is not needed anymore, you only call the particular function you want to use

# Importing everything from the module
from math import *
print(sqrt(100))
print(e)



# CREATING MY OWN MODULE
# Step 1: Create a folder and name it my_module
# Step 2: Create a file inside the folder and name it my_first.py
# Step 3: Create another file inside the same folder and name it my_second.py
# Step 4: Create another file still inside the same folder and name it my_main.py


# PYTHON PACKAGES
# A python package is a means of organizing related modules together into a folder. Inside this folder, there must be a special file caled __init.py__(the purpose of this file is to tell python to treat the folder as a package , and the file can be left empty)

# HOW TO INSTALL PYTHON PACKAGES

# 1. Using pip: This is the most common method. It installs packages from from PyPi which is Python's central package repository. To work with it, the terminal must be used.

# pip install requests              This installs tthe latest version
# pip install requests==3.27        This installs a specific version
# pip install --upgrade requests    This upgrades the eexisting package
# pip uninstall requests            This removes a package


# 2. Using uv: This is the modern, super-fast package and project maager. It is RUST-based, such that it unifies pakage installation, virtual environment and python version management into one fast, modern CLI

# To use uv, some commands must be run on the terminal depending on the Operating Syetem. The recommended method is to use a Stand-alone Installer

# For macOS or Linux,
#curl -LsSf htps://astral.sh/uv/install.sh | sh

# For Windows
# powershell -ExecutionPolicy ByPass -c "irm https://asstral.sh/uv/install.ps1 | iex"

# To verify the version after installation use:     uv --version
# For uv to work, you need to have a virtual environment


# CREATING A VIRTUAL ENVIRONMENT
# python -m venv virtual_environmnt_name    # Type this command in a command prompt or terminal. This will create a folder with the name virtual_environment_name. But to use the environment, it has to be activated.
# To activate the virtual environment, take the following steps
# 1. Click on the folder
# 2. Look for thee script and open it
# 3. Look for 'activate' 
# 4. Right click on itt and look for copy path
# 5. Click on it
# 6. Finally go to the terminal and select command prompt. Open the command prompt and copy the path you  just copied

# Alternatively, you can use ```
#virtual_environment_name\Scripts\activate  # For windows

# source virtual_environment_name/bin/activate # linux or macOS
#'''

# To deactivate





































































































