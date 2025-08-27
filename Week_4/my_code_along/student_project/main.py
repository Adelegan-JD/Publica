# main.py

# This file is the entry point to run the project

import data
import utils

# Add some students
data.add_student("Paul", "AI Engineering")
data.add_student("Blessing", "AI Development")
data.add_student("Abigail", "Python Development")
data.add_student("Forunate")

# Print formatted student records
for s in data.get_students():
    print(utils.format_student(s))


























































