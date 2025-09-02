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


expenses = []
date = dt.date(input("What date did you make this purchase? Please use this format: 25-12-1996 : "))
amount = float(input("How much do you spend daily?: "))
category = input("What category would you classify ths payment into: ")
description = input("Describe what you used the money for: ")

if date == dt.date():
    print("")

expenses.append({"date": date, "category": category, "amount": amount, "description": description})
header = ["date", "category", "amount", "description"]

file_path = Path.cwd()
csv_file = file_path / "expense_tracker.csv"

def add_expenses(expenses ):
    return expenses
with open(csv_file, "a+", encoding="utf-8") as doc:
    writer = csv.DictWriter(doc, fieldnames=header)
    for (key, values) in expenses.items():
        print("Expense tracker")

# with




















































