# Email slicer





# @title 13. Email Slicer(Extract Username from Email)

"""
Overview An Email Slicer is a simple yet useful tool that
extracts the username and domain from an email address.
This project enhances understanding of string manipulation,
user input handling, and string slicing in Python.
This project covers the step-by-step implementation of an
Email Slicer, including handling user input, extracting the
username and domain, and displaying the results.

Key Concepts of Email Slicer in Python

String Manipulation:

- Using string methods like split() and
- Extracting specific parts of a string

User Input Handling:

- Accepting an email address from the user
- Validating the input format

Output Formatting:

- Displaying extracted username and domain clearly
"""

# ### Syntax Table

# # | S/N | Concept         | Syntax/Example                                    | Description                               |
# # |-----|------------------|--------------------------------------------------|-------------------------------------------|
# # | 1   | Get user input   | `email = input("Enter your email: ")`           | Takes email address as input              |
# # | 2   | Split email      | `username, domain = email.split('@')`           | Splits the email into username and domain |
# # | 3   | Display result   | `print(f"Username: {username}, Domain: {domain}")` | Prints extracted username and domain     |


# # email = input("Kindly enter your email address")
# # username = email.split('@')[0]
# # domain = email.split('@')[1]


# while True:
        
#         email = input("Kindly enter your email address: ").upper()
#         username = email.split('@')[0].upper()
#         domain = email.split('@')[1].lower()
#         # corporate = email.endswith("@gmail.com", "@yahoo.com", "@hotmail.com")
#         # personal = email.endswith("@gmail.com", "@yahoo.com", "@hotmail.com") == False

#         if '@' not in email and '.' not in email:
#             print("Invalid input. Please use a correct address. Thank you.")
#         # elif email.endswith(".com") == False or email.isnumeric():
#         #      print("You can only start with letters")
#         else: 
#             print(f'Hello {username}, your domain name is @ {domain}')
             
#         choice = input("Please select 1 to continue or 0 to stop: ")
#         if choice == "0":
#             print("Thank you for using our service. Goodbye")
#             break
#         elif choice == "1":
#             continue
#         else:
#             print("Invalid selection. Please choose 1 or 2")

    




















tasks = []

def add_task(task):
     while True:
        try:
            print("1. Add task\n2. Remove task\n3. Complete task")
            choice = input("Welcome. What task do you want to carry out?: ")
            if choice == "1":
                print("Great!")
                user_task = input("What task would you like to add?:")
                add_task()
            else:
                print("Inavlid input")
        except Exception:
            print("An error occured")

add_task(user_task)


































































