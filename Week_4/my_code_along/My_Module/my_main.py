# My_Module/my_main.py

import my_first
import my_second

# Using the functions in my_first.py file

print("\n==== Mathemtical Functions ====")
print("1. Addition:\t     7 + 14 =", my_first.add(7, 14))
print("2. Subtraction:     55 - 25 =", my_first.subtract(55, 25))
print("3. Multiplication:  30 * 20  =", my_first.multiply(30, 20))
print("4. Division:\t    360 / 12 =", my_first.divide(360, 12))

# Using the functions in my_second.py file
print("\n==== String Functions ====")
print(my_second.greet("Deborah Adelegan"))
print("The reverse of COMMUNICATON is", my_second.reverse_string("communication").upper())
print("The character count of the sentence written is ", my_second.count_characters("Though Python modules are powerful, they're quite easy to learn and work with"))
print("The Word Count of the sentence written is", my_second.count_words("Though Python modules are powerful, they're quite easy to learn and work with"))





























































































