# PYTHON OPERATORS
# Operators are special symbols used to in Python to perform operations on variables and values. The threee most common operators are: Comparison operators, Assignment operators and Logical Operators.

# COMPARISON OPERATORS

a = 10
b = 20

# Equal to
print(a == b)       # Output: False

# Not equal to
print(a != b)       # Output: True

# Greater than
print(a > b)        # Output: False

# Less than
print(a < b)        # Output: True

# Greater than or equal to
print( a >= 10)      # Output: True

# Less than or equal to
print(a <= 25)      # Output: True

# Use case example -- Student Exam Result
score = 75
print(score >= 50)      # True (Passed)
print(score < 50)       # False (Failed)
print(score == 100)     # False (Not full mark)


# ASSIGNMENT OPERATORS
# Assignment operators are used to assign values to variables. They can also combine an operation with assignment, so instead of writing x = x + 5,,  we can write x +== 5

# To assign a value
x = 10
print("initial value:", x)

# To assign incrementally
x += 5
print("After x += 5: ", x)

# To decrease and assign
x -= 2
print("After x -= 2: ", x)

# To increase geometrically
x *= 3
print("After x *= 3: ", x)

# To decrease geometrically
x /= 4
print("After x /= 4: ", x)

# Modulus, to get ONLY the remainder after a division
x %= 3
print("After x %= 3: ", x)

# To increase by squares
x = 4
x **= 2
print("After x **= 2: ", x)

# To get floor division
x //= 3
print("After x //= 3: ", x)


# Use Case Example:

# Define variable
balance = 1000
deposit = 200
withdraw = 150

balance += deposit      # Add deposit
balance -= withdraw    # Subtract withdrawal

print("Updated Balance: ", balance)
# Output: Updated Balance: 1050


# LOGICAL OPERATORS
# Logigcal operators are used to combine conditional statements. They work with Boolean values(True or False)

# Define variables
x = 10
y = 20

# AND operator
print(x > 5 and y < 15)     # Output: True

# OR operator
print(x < 5 or y > 15)      # Output: True

# NOT operator
print(not(x == 10))     #  False


# Use cases.
# Example 1 - Scholarship Eligibility
# Define variables
age = 17
score = 85

# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)
print("Scholarship Eligibility: ", eligible)
# Output: Scholarship Eligibility:  True

# Use Case Two -  Event Access
age = 22
has_ticket = False

can_enter = (age>= 18) and (has_ticket or age < 25)

print("Access Granted: ", can_enter)
# Output: Access Granted:  True

















