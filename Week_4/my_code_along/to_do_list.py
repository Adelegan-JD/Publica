# @title 2. To-Do List Application

"""
A to-do list application is a practical project that
 helps users manage tasks efficiently. This application allows
 users to add, remove, and view tasks while keeping track of
 completed and pending activities. Learning to build a to-do
 list enhances understanding of data structures, file
 handling, and basic user interaction in Python.
 This project will cover step-by-step implementation of a to
do list application, user input handling, list operations, and
 file handling for persistent storage.

 Key Concepts of To-Do List in Python
 Basic List Operations:
 -Adding tasks
 -Removing tasks
 -Marking tasks as complete
 -Displaying tasks
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user inputs
"""
# I need to create functions for adding tasks and removing tasks
# Before then, create a list of tasks
tasks = []

# Now define the function for the addition of tasks
task = input("What task do you want to carry out? You can fill in as many tasks as possible. Just separate them with commas: ")
def add_tasks(*task):
    return str(tasks.append(task)).split(',')

# Define a function for removing tasks
removed_task = input("Please enter what task you want to remove from the list: ")
def remove_task(x):
    if removed_task in tasks:
        return tasks.remove(x)
    else:
        print("Oops! The task you just mentioned is not present in the list of tasks")

# Define a function for marking tests as complete
def completed_task(*done_task):
    done = input("Please enter the task you have completed any task and not yet if you aren't done")
    if done == "done":
        print(f"Welldone! You have completed {done_task}.")
        if done_task in [tasks]:
            return tasks.remove(done_task)





print(tasks)
add_tasks()
print(tasks)
remove_task(removed_task)
print(tasks)
completed_task()
print(tasks)















































































