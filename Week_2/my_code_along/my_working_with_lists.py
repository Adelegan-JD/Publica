# HOW TO CREATE A LIST
# You can create an empty list when you don't have elements yet but plan to add it later.

# Method 1: Using square brackets
empty_list = []
print(empty_list)       # Output = []

# Method 2: Using the list() constructor
empty_list2 = list()
print(empty_list2)


# CREATING A LIST WITH INITIAL ELEMENTS
# List oof integers
numbers = [1,2, 3, 4, 5]
print(numbers)  # Output: [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry", "mango", "raspberry"]
print(fruits)   # Output: ['apple', 'banana', 'cherry', 'mango', 'raspberry']

# Mixed Data Types
mixed_list = ["Alice", 25, 5.7, True]
print(mixed_list)

# Creating a List from another sequence. You can convert strings, tuples, or otther iterables into a list
# From a string (each character becomes an element)
chars = list("hello")
print(chars)    # Output: ['h', 'e', 'l', 'l', 'o']

# From a Tuple
my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)  # [10, 20, 30]

# From a Range
numbers_range = list(range(5))
print(numbers_range)    # Output: [0, 1, 2, 3, 4]

# Creating a  list using list comprehension. They are a concise way to create lists using a loop in one line.
# Squares of numbers 0-4
squares = [x**2 for x in range((5))]
print(squares)  # [0, 1, 4, 9, 16]

# Even numbers between 0 to 10
evens = [x for x in range(11) if x % 2 == 0]
print((evens))  # Output: [0, 2, 4, 6, 8, 10]

# Creating a Nested List. A list can contain other lists. It is used for matrices or grouped data.

# Matrix-like list 
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(matrix)      # Output: [[1, 2] [3, 4], [5, 6], [7, 8]]

# Accessing elements in a list
print(matrix[0])    # Output: [1, 2]
print(matrix[0][1]) # Output: 2
print(matrix[1])    # Output: [3, 4]
print(matrix[1][0]) # Output: 3
print(matrix[1][1]) # Output: 4


# Characteristics of a String

# 1. It is ordered
fruits = ["mango", "orange", "banana", "kiwi"] 
print(fruits)   # ['mango', 'orange', 'banana', 'kiwi']
print(fruits[0])    # mango (first element)
print((fruits[2]))  # banana (third element)

# 2. It allows duplicates
items = ["rice", "bans", "yam", "rice"]
print(items) # # Output: ['rice', 'beans', 'yam', 'rice]

# 3. It is mutable i.e. it can be changed, replaced, removed from, or added to.
numbers = [1, 2, 3, 4, 5, 6]
numbers[2] = 43
print(numbers) # Output: [1, 2, 43, 4, 5, 6]

# 4. It can contain different data types
mixed = [10, "Nigeria", 3.24, True]
print(mixed)    # Output: [10, 'Nigeria], 3.24, True

# 5. It can be nested i.e. it can contain other lists(2D or multi-dimensional lists)
nested_list = [[1, 2], ["q", "w"]]
print(nested_list)
print(nested_list[0][1])    # Output: 2

# 6. It has dynamic size, i.e you don't need to declare the size of a list beforehand: it can grow or shrink as needed
name = ["Ada", "Bola"]
name.append("Caleb")
print(name) # Output:['Ada', 'Bola', 'Caleb', 'Daniel']


# LIST OPERATIONS IN PYTHON

# 1. Concatenation (+). It joins two lists into a single list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 +list2
print(result)   # Output: [1, 2, 3, 4, 5, 6]

# 2. Repitition. This repeats the elements in a lista given number of times
nums = [1, 2]
repeated = nums * 5
print(repeated) # Output: [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

# 3. Indexing  This is used to access elements using their positions(starting from zero)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # apple
print(fruits[-1])   # cherry (negative indexing starts from the end)

# 4. Slicing    This is used to extract a portion of the list
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])     # [1, 2, 3]
print(numbers[:3])      # [0, 1, 2]
print(numbers[3:])      # [3, 4, 5, 6]
print(numbers[::2])     # [0, 2, 4, 6]  step of 2

# 5. Membership (in/not in). It checks if an element exists in a list
colors = ["red", "green", "blue", "purple"]
print("green" in colors)        # True
print("indigo"  in colors)      # False
print("yellow" not in colors)   # True
print("purple" not in colors)   # False

# 6. Length (len())     This counts the numbers of elements in a list
items = ["pen", "book", "laptop"]
print(len(items))   #3

# 7. Min and Max (min()/max())




