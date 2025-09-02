# @title 17. Basic Expense Tracker
"""
An Expense Tracker is a practical application that
allows users to log their daily expenses and track spending
habits. This project enhances knowledge of file handling,
data storage, and user input processing in Python.
This chapter covers the step-by-step implementation of an
Expense Tracker, including user input handling, data storage
in a CSV file, and displaying expense reports.

Key Concepts of Expense Tracker in Python

Data Handling:

Using lists and dictionaries to store
expenses
Writing and reading data from a CSV file

User Input Processing:

Taking user input for expense details
Validating and formatting input data

Report Generation:

Displaying total expenses per category
Summarizing daily or monthly spending

"""


# | SN | Concept            | Syntax/Example                                                            | Description                          |
# | -- | ------------------ | ------------------------------------------------------------------------- | ------------------------------------ |
# | 1  | Import CSV module  | `import csv`                                                              | Enables reading/writing to CSV files |
# | 2  | Get user input     | `amount = float(input("Enter amount: "))`                                 | Takes expense details from the user  |
# | 3  | Store expenses     | `expenses.append({"date": date, "category": category, "amount": amount})` | Saves expense data in a list         |
# | 4  | Write to CSV file  | `with open("expenses.csv", "a") as file:`                                 | Appends expense data to a CSV file   |
# | 5  | Read from CSV file | `csv.reader(file)`                                                        | Reads stored expenses from the file  |

from pathlib import Path
import csv
import datetime as dt

# create an empty task list. then create an functions for the user to input the task
tasks = []


#create function to add task

def task_add(user_task):
    while True:
        try:
            if user_task == " ":
                print("Input can't be empty")
            elif user_task.isdigit():
                print("Can't be number")
            else:
                tasks.append(user_task)
        except ValueError:
              print("Can't be number")
        except Exception as e:
              print(f"Unexcepted error occurred: {e}")
                        
def main():
    while True:
        try:
            print("1. Add Task  2. Remove Task  3. View Tasks")
            choice = input("Enter the operation you want to do: ")
            if choice == "1":
                user_task = input("Enter the task you want to add: ")
                task_add(user_task)
                return "Task Successfully added!"
            else:
                print("Invalid option")
        except Exception:
            print("Error occurred")
# if __name__ = ""
main()






# def add_task(task):
#         input_task = input("Please enter a task you want to do: ") 
#         return tasks.append(task)
# add_task()

# #create function to remove task
# def remove_task(task):
#         removed_task = input("Please enterr the task you want to remove: ")
#         if removed_task in tasks:
#                 return tasks.remove(removed_task)
#         else:
#                 print(f"Oops! {removed_task} is can not be found in your to-do list. Please check again carefully.")
#                 print(tasks)
# remove_task()

# #create fuunction for done tasks
# done = input("Please enter which task you want to mark as done")
# def done_tasks(*task):
#         if done in tasks:
#                 print (f"Great! You have completed {task}. It will now be marked done")
#                 return f"\"{tasks[task]}\" - done"
#         else:
#                 print("This task is not in your list of tasks")
# done_tasks()

# print(tasks)
















































