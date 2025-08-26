# Single Quotes
name = 'Ada'

# Double Quotes
greeting = "Hello"

"Triple Quotes (for multi-line strings)"
story =  '''Once upon a time,
there was a girl named Ada.'''

# String with numbers and symbols
password =  "p@ssw0rs123"

# Eplanation
# Single quotes and double quotes work the same way.
# Triple quotes allow your string to span across multiple lines without using \n.
# Strings can contain letters, numbers, spaces and special characters.
# In Python, there is no "character"type - even a single letter is considered a string.

# STRING OPERATIONS
# Indexing
word = "There is something called alphabeticcal order in English Language. It is the arrangement of alphabets from A to Z. English Language is a universal language accepted in many counteries but fully understood by few. It is great to learn the syntax of English Language"
len(word)   # This gives the length of the word, including alphabets and characters
sentence = word.split()   # This splits or breaks the sentence into word by word
print(sentence)
len(sentence)  # This generates the length of each word
print(sentence[0])   # This prints out or indexes the first word because Python starts its counting fom zero not one

# Slicing
print(sentence[0:4])   # This slices the first four words in the sentence
print(sentence[2:])    # This slices the second word and every other word after it
print(sentence[:3])    # This slices the first three words. It generates all the words that come before the index 3
print(sentence[::2])   # This generates the entire sentence, but skips it by one word. It prints out the words in second order
print(sentence[::-1])  # This generates the sentence in reverse order, starting from the last word to the first word.



# STRING CONCATENATION AND REPITITION
# Concatenation
a = "Hello" 
b = "World"
print(a+b)

# Repitition
word = "Hi! "
print(word * 3)   # This generates Hi! Hi! Hi!

# STRING SEARCHINGG AND CHECKING
# Membership
text = "Python Programming"
print("Python" in text)      # True
print("Java" not in text)    # True
print("Python" not in text)  # False
print("Programming" not in text) # False

# Find() / RFind()
text = "Hello World"
print(text.find("o"))   # Finds and prints out the index number of "o" which is 4
print(text.rfind("o"))   # Finds again and prints out the index number of "o" which is 7

# Index() / RIndex()
# It is just like find()  but it will raise an error if the element is not found
text = "Hello World" 
print(text.find("o"))    # 4
print(text.index("World"))  # string
print(text.index("happy"))   # will generate a ValueError - "NotFound"

#startswith() /endswith()
filename = "data.csv" 
print(filename.startswith("data"))   # True



# STRING OPERATIONS

# Creating and manipulating strings
# upper()   to convert all the letters to uppercase
# lower()   to convert all the lettes to lowercase
# title()   to make the first letter of every word uppercase
# strip()   to remove all whitespace like tab spaces and the likes of it
# replace() to replace a letter or a word in a sentenece or string


# upper()   to convert all the characters in the string to uppercase
name = "Ada Balogun"
print(name.upper())
# Output: ADA BALOGUN

# lower() converts all characters in the string to lowercase
sentence = "PYTHON IS Amazing"
print(sentence.lower())
# Output: python is amazing

# title() converts only the first character of each word to uppercase
statement = "mary is an inquisitive learner"
print(statement.title())
# Output: Mary Is An Inquisitive Learner

# strip() removes the whitespace (or specified characters) from both ends of thhe string.
text = "    Abuja   "
print(text.strip())
#Output: Abuja

# replace()   This replaces occurences of a substring with another substring
message = "I love Java"
print(message.replace("Java", "Python"))
# Output: I love Python

# swapcase()   switches lowercasee to uppercase and vice versa
text = "Hello ABEOKUTA"
print(text.swapcase())
# Output: hELLO abeokuta

# lstrip()  removes whitespace (or specified characters) from the left side only
text = "    Nigeria"
print(text.lstrip())
# Output: Nigeria

# rstrip()
text = "Nigeria      "
print(text.rstrip())

# split()    splits a string into a list using a separator (default is space)
fruits = "mango orange banana"
print(fruits.split())

# rsplit()      splits a string into a list from the right side
text = "one,two,three,four,five,six"
print(text.rsplit(",", 2))

# splitlines()          splits a string into a list at each newline(\n)
lines = "Line 1\nLine 2\Line 3"
print(lines.splitlines())

# join()        joins a list of srings into one sring with a specified separator
words = ["I", "love", "Python"]
print(" ".join(words))
# Output: I love Python

# center()      centers the string within a specified width, padding with spaces or characters
text = "Python"
print((text.center(20, "-")))
# Output: -------Python-------

# ljust()       left-aligns the string within a specified width, padding withh spaces or characters
text = "Python"
print(text.ljust(10, "-"))
# Output: Python----

# rjust()       right-aligns he string within a specifieed width, padding with spaces or characters
text = "Python"
# Output: ****Python

# zfill()       pads a numeric string on the left with zeroes until it reaches a given length
num = '42'
print(num.zfill(5))
#3 Output: 00042

# isalpha()     checks if the strings contains only letters
print("Lagos".isalpha())        # True
print("Lagos123".isalpha())     # False

# isdigit()     checks if the string contains only digits
print("12345".isdigit())        # True
print("123A".isdigit())     # False

# isalnum       checks if the string contains only letters and digits
print("Python3".isalnum())      # True
print("Python 3".isalnum())     # False
























































































