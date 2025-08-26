# PYTHON DICTIONARIES
# Adictionary in Python is a collection of key-value pairs. 
# Keys are unique and used to sttore and retrieve values
# Values can be any data type (string, integer, list, tuple, even another dictionary)

# Characteristics of Dictionary

# 1. Dictionaries have a key-value structure i.e. each item is stored as a key:value pair
# 2. Thay are mutable
# 3. They are unordered
# 4. They have unique keys i.e no duplicate keys are allowed
# 5. Keys must be immutable

# CREATING DICTIONARIES
# 1. Using curly braces
# student = {"name": "Ada",
#            "age": 20,
#            "course": "Computer Science"
# }
# print((student))        # Output: {'name': 'Ada', 'age': 20, 'course': 'Computer Science'}

# # 2. Using the dict() constructor
# student_info = dict(name ="John", age = 25, course = "Maths")
# print(student_info)     # Output: {'name': 'John', 'age': 25, 'course': 'Maths'}

# # 3. Empty dictionary
# empty_dict = {}
# print(empty_dict)       # Output: {}

# # DICTIONARY COMPREHENSION
# # Syntax:
# # {key_expression: value_expression for item in iterable if condition}

# # Create a dictionary of numberrs and theirr squares
# squares = {x: x**2 for x in range(1, 9)}
# print(squares)      # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# # With Condition
# # Dictionary of even numbers and their cubes
# evens_cube = {x: x**3 for x in range(1, 15) if x % 2 == 0}
# print(evens_cube)       # Output: {2: 8, 4: 64, 6: 216, 8: 512, 10: 1000, 12: 1728, 14: 2744}

# # From existing dictionary
# students = {"Ada" : 85, "John" : 40, "Chidi":67, "Musa":65}
# # Filter students who passed (score >= 50)
# passed_students = {name: score for name, score in students.items() if score >= 50}
# print(passed_students)      # {'Ada': 85, 'Musa': 65}

# # Using String Keys
# names = ["Ada", "John", "Musa", "Abigail"]
# lengths = {name: len(name) for name in names}
# print(lengths)      # Output: {'Ada': 3, 'John': 4, 'Musa': 4, 'Abigail': 7}


# # ACCESSING DICTIONARY ITEMS

# # Define a dictionary
# student = {"name": "Ada", "age": 20, "course": "Computer Science"}

# # Using Key
# print(student["name"])      # Output: Ada

# # Using get() method (avoids error if key is missing)
# print(student.get("age"))
# print(student.get("grade", "Not Found"))        # Output: 20, Not Found

# # MODIFYING DICTIONARIES
# student["age"] = 21     # This changes the value
# student["grade"] = "A"      # This adds a new key-value pair
# print(student)      # Output: {'name': 'Ada', 'age': 21, 'course': 'Computer Science', 'grade': 'A'}

# # Removing Items From Dictionaries
# # 1. Using pop()
# student.pop("grade")

# # 2. Using popitem() - removes the last inserted key-value
# student.popitem()

# # 3. Using del keyword
# del student["age"]

# # Usinig clear() - this removes all items
# student.clear()

# print(student)      # Output: {}

# # DICTIONARY METHODS
# # dot keys(), dot values(), dot items(), dot update()
# person = {"name": "Emeka", "age": 30}

# # 1. keys()
# print(person.keys())        # Output: dict_keys(['name', 'age'])

# # 2. values
# print(person.values())      # Output: dict_values(['Emeka', 30])

# # 3. items()
# print(person.items())       # Output: dict_items([('name', 'Emeka'), ('age', 30)])

# # 4. update()
# person.update({"age": 31, "city": "Lagos"})
# print(person)       # Output: {'name': 'Emeka', 'age': 31, 'city': 'Lagos'}

# # NESTED DICTIONARIES
# students = {
#     "student1":{"name": "Ada", "age": 20},
#     "student2":{"name": "John", "age": 22}
# }
# print(students["student1"]["name"])   # Access nested data
# # Output: Ada

# # LOOPING THROUGH DICTIONARIES
# # Define a dictonary
# student = {"name": "Ada", "age": 20, "course": "Computer Science"}

# # Loop through keys
# for key in student:
#     print(key)      # Output: name, age, course

# # Loop through values
# for value in student.values():
#     print(value)        # Output: Ada, 20, Computer Science

# Loop through value-pairs
# student = {"name": "Ada", "age": 20, "course": "Computer Science"}
# for key, value in student.items():
#     print(f"{key}: {value}")        # Output: name: Ada, age: 20, course: Computer Science

# Storing a student's biodata
student = {
    "name": "Blessing",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}
print(f"Name: {student['name']}")
print(f"Subjects: {', '.join(student['subjects'])}")
# Output: Name: Blessing
# Subjects: Maths, Physics, Chemistry

# ADDING KEY-VALUE PAIRS TO A DICTIONARY
# Create an empty dictionary
student = {}

# Add key-value pairs to it
student["name"] = "Goodness"
student["Interest"] = "AI"
student["Track"] = "AI_Dev"

print(student)

# LIST OF DICTIONARIES
# List of dictionaries - Each student has their own dictionary
students = [
    {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
    {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
]

print(students[0]["Name"])   
print(students[1]["Track"])

# DICTIONARY OF DICTIONARIES
# Dictionary of dictionaries - Each student is keyed by their ID
students = {
  "AI010"   :  {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
  "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}

print(students["AI020"]["Name"])   
print(students["AI030"]["Track"])

# Dictionary of lists - Each subject stores a list of scores
scores = {
    "python": [85, 78, 92],
    "pandas": [88, 74, 90],
    "Scikit-learn": [80, 95, 87]
}

print(scores["python"])    
print(scores["pandas"][1])  
























