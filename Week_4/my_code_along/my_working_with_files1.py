# import the operating system
import os

# Get the current working directory
print(f"This is my current working directory:, \"{os.getcwd()}\"")

#There are two types of paths
# 1. Absolute Path: This is the full address of a file, like a complete GPS
absolute_path = r"C:\Users\ncc\Desktop\my_virtual_environment"      # The purpose of using "r" before writing the path is soo as to make python know thet the forward or backward slash used in the code are not escape sequences and should not be treated as such.

# 2. Relative Path: This is a shortcut tha starts ffrom the current working folder
relative_path = "my_path.py"

print("The Absolute Path is: ", absolute_path)
print("The Relative Path is: ", relative_path)


# JOINING PATHS THE RIGHT WAY

import os
folder =  "C:/Users/ncc/Desktop"
filename = "my_path.py"

path  = os.path.join(folder, filename)
print("The full path is: ", path)

# CHECKING IF A FILE OR FOLDER EXISTS
# To do this, we can use os.paths.exists

import os

path = "my_path.py"

if os.path.exists(path):
    print("Yes, the file exists")
else:
    print("File Not Found")


# USING PATHLIB(MODERN WAY)
# Python has a modern library called "pathlib", which is easier touse than "os"

from pathlib import Path

# To get the current working dirrectory
print("My current workng directory is", Path.cwd())

# To create  Path object
file = Path("myfile.txt")

# To check if the path object or file exists
print("File exists: ", file.exists())

# To combine paths
folder =Path("C:/Users/ncc/Desktop")
full_path = folder / "myfile.txt"
print("Full Path:", full_path)
print(file.exists())


# Navigating folders with pathlib

from pathlib import Path

# To get the parent folder of the current file
print(f"The parent folder is \"{Path.cwd().parent}\"")

# List all files in a directory
for file in Path.cwd().iterdir():
    print(file)























