# # # INTRODUCTION TO MODULARITY

# # # Modular programming is a way of writing programs by dividing them into 
# # # smalle, independent, and reusable parts

# # # Common  Categories of Built-In Functions

# # # 1. Input and Otput Functions
# # print() # displays output
# # input()  # takes user input()

# # # 2. Type Conversion Functions
# # int(), float(), bool(),  list(), dict(), tuple(), set()

# # # 3. Mathematical Functions
# # abs()       # Absolute value
# # pow(x, y)       # x raised to power y
# # round()     # Rounds numbers to the defined decimal place
# # min(), max(),       # Finds the smallest/largest figure

# # # 4. Sequence and Collection Functions
# # len()      # Provides the length  of a sequence
# # sum()       # Provides the sum of elements
# # sorted()        # Sorts items
# # enumerate()     # Tracks index and value

# # # 5. Utility Functions
# # type()      # showa the type of an object(variables, data types, data structures, function, classes)
# # id()        # returns the unique ID of an object in meory
# # help()      # Provides the documentation of an object

# # # 6. Special Built-ins
# # range()     # Generates a sequence of numbers
# # zip()       # Combines two lists, elememnt by element
# # map()       # Applies a function to all elemnts in a sequence
# # filter()        # Filters elements in a sequence based on condition


# # # EXAMPLES OF USE

# # 1. range
# for i in range(3):
#     print(i)        # Output: 0, 1, 2

# # 2. zip()
# names = ["Esther", "Precious", "Kennie"]
# scores = [85, 90, 95]
# for n, s in zip(names, scores):
#     print(n, "scored", s)       # Esther scored 85; Precious scored 90; Kennie scored 95

# # 3. map()
# nums = [1, 2, 3, 4]
# squared= list(map(lambda x: x**2, nums))
# print(squared)      # Outpu: [1, 4, 9, 16]

# # 4. filter()
# even_nums = list(filter(lambda x: x % 2 ==0, nums))
# print(even_nums)        # Output: [2, 4]


# # STUDENT PERFORMANCE AND FEEDBACK SYSTEM
# # Step 1:Input student's data
# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + " here: "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + " here: "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + " here: "))

# # Step 2: Sttore in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # Step 3: Display data
# print("\nStudent Data")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# # Step 4: Summarize using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\n Performance Summary: ")
# print("Total Score: ", total)
# print("Average Score: ", average)
# print("Highest Score: ", highest)
# print("Lowest Score: ", lowest)

# # Step 5: Ranking (Using Sorted and Zip)
# ranked = sorted(zip(scores, names), reverse = True)
# print("\n Ranking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# # Step 6: Check your data types
# print("\n Data Type Checks: ")
# print("Type of names: ", type(names))
# print("Type of scores: ", type(scores))
# print("ID of names list: ", id(names))
# print("ID of scores list: ", id(scores))

# # Step 7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing Scores: ", passing)

# # Step 8: Map names to uppercase
# uppernames = list(map(lambda n: n.upper(), names))
# print("Uppercase Names: ", uppernames)

# # Step 9: Use help() to show documentation of len, type and list
# print("\n Help on len():")
# help(len)

# print("\n Help on type():")
# help(type)

# print("\n Help on list():")
# help(list)






# # USER DEFINED FUNCTION
# # In python, the def function is used to define a function. Then we call the function wheneve we want to use it
# # Python Function Structure
# # def function_name(takes in input):
# #     process block/logical line
# #     output block

# # More explanation

# # def function_name(input - here, you will insert an item or list of what the function will need to work):

# #     "process block -here will contain the logic or what you want the function to do"

# #     " output - Then here will contain what you want the function to output. You can either use the 'return' keyword or'print()' or 'yield'"


# DEFINING A FUNCTION
def greet():
    print("Hello, welcome to AI Fellowship!")

# When a function is being used, this is how to call it, and it can be called asmany times as possible
greet()
greet()
greet()

# Function Arguments and Parameters
# Arguments are variables you add inside the function parenthesis when defining the function(placeholders). Sometimes, they can be optional
# Parameters are the actual values you pass inside the function parenthesis when calling the function

# Function with an Argument - The placeholder
def greet(name):
    print("Hello ", name, " welcome to Python Learning!")

# Calling with parameter - the actual name
greet("Class Rep")
greet("Toluwanimi")

# When to use Return, Print() and Yield keywords inside a function

# 1.  The print() keyword is used when you are only interested in displaying your output without storing it.

def greet(name):
    print("Hello, name")

# Function Call
result = greet("Esther")

# The result here is empty because it has not been previously recorded
print("Result:", result)       # Output: Result: None


# 2. Return
# The return keyword is used when you want to give back a value. Return sends a value back to the function caller. 
# The function ends immediateely after the return is used.

def add(a, b):
    return a + b

# Function call

result = add(5, 8)
print("The sum is:", result)        # Output: The sum is: 13

# 3. Yield 
# This is used for producing a sequence(a generator). Yield works like return, but instead of ending the function, it pauses and remebers its state. Next time it is called, it can resume from where it stopped
# This creates a generator, and it can be used when working with large data or infinite spaces

def count_up_to(n):
    i = 1
    while i <= n:
        yield i     # pause and return i
        i += 1

# Using the generator
for number in count_up_to(5):
    print(number)
# In this case, instead of giving all numbers at once, the function yields them one at a time

# Types of Function Arguments
# Functions can accept different types of arguments depending on how data is beiing passed. 

# 1.POSITIONAL ARGUMENTS: They are the most common, and they are very strict with orderly arrangement. 
def introduce(name, track):
    print("My name is ", name)
    print("I am in the", track, "Track.")   
# Output: My name is  Ngozi
# I am in the AI Development Track.

# Function call
introduce("Ngozi", "AI Development")        # This is the correct order: name, then track

# Trying the incorrect order will generate a "Semantic" error
introduce("AI Engineering", "Tobi")
# Output:
# My name is  AI Engineering
# I am in the Tobi Track.

# 2. KEYWORD ARGUMENTS: In this case, the parameter name must be mentioned. Order does not matter here, since Python knows which values go where.

def introduce(name, track):
    print("My name is", name)
    print("I am learning", track)

# function call
introduce(name = "Ngozi", track = "AI Engineering")

# Changing the arrangement
introduce(track = "AI Engineering", name = "Ngozi")     # In this case, order does not matter


# 3. DEFAULT ARGUMENTS: Here, parameters can be given a default value. And even if no value is provided when calling, the default is useed.
def introduce(name, track = "AI Engineering"):
    print("My name is", name)
    print(f"I am learning", track, ".")

# Function call, but without specifying the output 
introduce("Paul")


# Specify the default argument
introduce("Tunji Paul", track = "AI Development")

# VARYING LENGTH ARGUMENTS:  Sometimes, the number of arguments that will be passed may not be known.Python provides two special symbols(which is the asterisk. The single asterisk is for non-keyword arguments or tuple(*args) and the Double asterisk is for keyword arguments or dictionaryy(**kwargs)
# A. Non-keyword Arguments(tuple): This collects extra positional arguments into a tuple.
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

# function call
# Take note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)

# B. Keyword Arguments(Dictionary): This collects extra keyword arguments into a dictionary. It is like a labeled container where each item has a name tag.

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Function call
student_details(Name = "Peter", Track = "AI Engineering", Interest = "Block Chain")

# IMPLEMENTING A FULL CODE
def participant_profile(name, age, track = "AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n--- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    # Skills (from *args)
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"

    # Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
    for key, value in extra_info.items():
        profile += f" - {key.capitalize()}: {value}\n"

    return profile  # Return keyword is being used so that the function can be reused in other places.


# Example 1. Using only positional arguments
print(participant_profile("Peter", 24))
# Output
#--- Bootcamp Participant Profile ---
# Name: Peter
# Age: 24
# Track: AI Development
# Skills: Not yet specified

# Example 2: Adding keyword/default argument
print(participant_profile("Ridwan", 29, track="AI Engineering"))
# Output
# --- Bootcamp Participant Profile ---
# Name: Ridwan
# Age: 29
# Track: AI Engineering
# Skills: Not yet specified

# Example 3: Adding a variable-length positional arguments (*args)
print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))
# Output:
# --- Bootcamp Participant Profile ---
# Name: David
# Age: 27
# Track: Data Science
# Skills: Python, SQL, Machine Learning

# Example 4: Adding variable-length keyword arguments (**kwargs)
print(participant_profile(
    "Sophia", 30, "Cybersecurity"
    "Networking", "Ethical Hacking", "Python",
    interest = "Blockchain", city = "Shagamu", Phone = "08123456789"
))

# NAMESPACES AND SCOPE
# A namespace is like a "container" that holds names(variables, functions, objects and maps).
# It is like a dictionary where keys are names and values are objects. Python uses namespaces to avoid name conflicts. 

# TYPES OF NAMESPACES
# 1. Built-in Namespace: This is provided by python (e.g., len, print, list)
# 2. Global Namespace: These are namees defined at the top level of a script or module
# 3. Local Namespace: These are names created inside a function

# Using Built-in Namespace Function
print("Length of 'Python:", len("Python"))

# Global Namespace
employee = "General Employee"

def IT_Department():
    # Local Namespace inside IT_Department
    employee = "Chris (IT)"
    print("Inside IT Department:", employee)

def Training_Department():
    # Local Namespace inside Training_Department
    employee = "Chris (Training_Department)"
    print("Inside Training Department:", employee)

print("In Global Namespace:", employee)     # Refers to global variable

IT_Department()         # Uses local variable in IT
Training_Department()   # Uses local variable in training



# SCOPE: Scope defines where in the code a name is accessible. Python follows the LEGB Rule(order of search for a variable)
# L - Local : Insidethe current function
# E - Enclosing : Inside any enclosing function(s)
# G - Global : At the top level of the script/module
# B - Built-In : Python's built-in functions/objects

# Use case
x = "global x"      # Global Namespace

def outer():
    x = "enclosing x"       # Enclosing Namespace

    def inner():
        x = "local x"       # Local Namespace
        print("Inside inner:", x)       # Local wins

    inner()
    print("Inside outer:", x)       # Enclosing

outer()
print("In global:", x)      # Global





































