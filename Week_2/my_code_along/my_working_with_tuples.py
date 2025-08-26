# # TUPLES
# # A tuple is an ordered, immutable (unchangable) collection of items in Python

# # Creating Tuples
# # 1. Using parentheses
# # Example 1: tuples with multiple items
# fruits = ("apple", "banana", "cherry")
# print(fruits)   # Output: ('apple', 'banana', 'cherry')

# # 2. Without parentheses
# numbers = 1, 2, 3, 4, 5, 6
# print(numbers)  # Output: (1, 2, 3, 4, 5, 6)

# # 3. Single Item Tuple(must includcle a comma)
# single_item = ("apple",)
# print(single_item)      # ('apple',)
# print(type(single_item))        # <class 'tuple'>

# 4. Using the tuple constructor
# fruits_list = ["apple", "banana", "cherry"]
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)     # ('apple', 'banana', 'cherry')


# Characteristics of Tuples
# 1. It is ordered
# colors = ('red', 'green', 'blue')
# print(colors[0])        # red

# 2. It is immutable
#colors[1] = "yellow"        # Output: TypeError: 'tuple' object does not support item assignment

# 3. It allows duplicates
numbers = (1, 2, 3, 2, 5, 2, 4, 3, 3, 6, 4)
print(numbers)  # Ouput: (1, 2, 3, 2, 5, 2, 4, 3, 3, 6, 4)

# 4. It allows for mixed data types
mixed = ("apple", 3, False, 5.78)
print(mixed)        # Output: ('apple', 3, False, 5.78)

# 5. It can be nested
nested = (("a", "b"), (1, 2), (True, False))
print(nested)       # (('a', 'b'), (1, 2), (True, False))


# TUPLE OPERATIONS
# 1. Tuple Indexing
fruits = ("banana", "apple", "cherry", "date")
print(fruits[-1])       # Output: date
print(fruits[1])        # Output: apple

# 2. Slicing
print(fruits[0:2])      # Output: ('banana', 'apple')
print(fruits[::-1])     # Output: ('date', 'cherry', 'apple', 'banana')

# 3. Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = (5,6)
result = tuple1 + tuple2 +tuple3
print(result)           # Output: (1, 2, 3, 4, 5, 6)

# 4. Repitition
nums = (1, 2)
print(nums * 4)     # Output: (1, 2, 1, 2, 1, 2, 1, 2)

# 5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)           # True
print("date" in fruits)             # False
print("grape" not in fruits)        # True
print("banana" not in fruits)       # False

# 6. Iteration
for fruit in fruits:
    print(fruit)


# WORKING WITH TUPLES
# Tuple Methods: Tuples have only two methods - dot count() and dot index()

numbers = (1, 2, 2, 3, 4, 5)
print(numbers.count(2))     # Output: 2
print(numbers.index(3))     # Output: 3

# Converting Between Lists and Tuples
# Tuple to List
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)      # Output: [1, 2, 3, 4]

# List back to tuples 
t = tuple(lst)
print(t)        # Output: (1, 2, 3, 4)

# BUILT-IN FUNCTIONS WITH TUPLES
nums = (4, 2, 4, 5, 7, 9, 12)
print(len(nums))        # Output: 7
print(max(nums))        # Output: 12
print(min(nums))        # Output: 2
print(sum(nums))        # Output: 43

















































































