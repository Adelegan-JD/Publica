#  A set is an unordered collection of unique elements.Sets are useful when you want to store multiple items but avoid duplicates.
# CRAETING SETS

# 1. Using curly braces
fruits = {"apple", "banana", "mango"}
print(fruits)           # Output: {'apple', 'banana', 'mango'}

# 2. Using the set() constructor
numbers = set([1, 2, 3, 4, 5, 6])
print(numbers)      # Output: {1, 2, 3, 4, 5, 6}

# 3. Creating an empty set (must use set(), not {})
empty_set = set()
print(empty_set)        # Output: set()

# 4. From a string (duplicates removed automatically)
letters = set("mississippi")
print(letters)      # Output: {'p', 's', 'i', 'm'}

# CHARACTERISTICS OF SETS
# 1. They are unordered
# 2. They have unique elemennts, i.e duplicates are automically removed
# 3. They are mutable, i.e you can add or remove items
# 4. They are unindexed, i.e you can't access elements using an index like my_set[]
# 5. It supports mathematical set operations, e.g. union, intersection, difference, symmetric difference

# SET OPERATIONS
# 1. Adding elements
colors = {"red", "blue"}
colors.add("green")
print(colors)       # Output: {'green', 'red', 'blue'}

# 2. Removing Elements
colors.remove("blue")       # This removes an element, raises an error if not found
colors.discard("yellow")        # This removes if found, but no does not raise an error if missing
print(colors)       # Output: {'green', 'red'}

# 3. Pop an element
colors = {"red", "blue", "green"}
removed = colors.pop()
print("Removed:", removed)
print("Remaining:", colors)      # Output:  Removed: green;; Remaining: {'red', 'blue'}


# 4. Clear a set
colors.clear()
print(colors)       # Output: set()


# MATHEMATICAL SET OPERATIONS
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# 1. Union
print(set1 | set2)
print(set1.union(set2))     # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9} ;; {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 2. Intersection
print(set1 & set2)
print(set1.intersection(set2))      # Output: {4, 5, 6} ;; {4, 5, 6}

# 3. Difference
print(set1 - set2)
print(set1.difference(set2))        # Output: {1, 2, 3} ;; {1, 2, 3}

# 4. Symmetric Difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))      # Output: {1, 2, 3, 7, 8, 9}
{1, 2, 3, 7, 8, 9}


# WORKING WITH SETS
# Collecting unique visitors to an event
visitors = set()

# Adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu")  # This is a duplicate, so it is automatically ignored
print("Visitors: ", visitors)       # Output: Visitors:  {'Aisha', 'Chinedu'}

# Checking if a visitor attended

name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")      # Output: Aisha attended the event.









































































































