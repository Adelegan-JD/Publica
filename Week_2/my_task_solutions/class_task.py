# TASK 1: Write a program to take a string input from the user and display it in uppercase
name = input("Kindly enter your name: ")    # This accepts the user's name
print(name.upper())


# TASK 2: Given the string "python", print its first and last characters
string = "python"
print(string[::5])


# TASK 3: Ask the user for thier name and print "Hello, !" where is the user's input
name = input("Kindly tell me your name: ")
print("Hello, " + name + "! ")


# TASK 4: Write a program to count the number of characters in a string without using len()
sentence = ""



# TASK 5: Given "Hello World", replace World with "Python"
text = "Hello, World"
print(text.replace("World", "Python"))


# TASK 6: Check if a given string contains the substring "python"(case-insensitive)
text = "Python programming"
print("python" in text)
print("Python" in text)


# TASK 7: Write a program to reverse a string without using slicing([::-1])
statement = ("Abracadabra")
full_statement = (statement[10])
print

# TASK 8: Given a string  with extra spaces, remove the leading and trailing spaces
sentence = "            Nigeria         "
print(sentence.lstrip().rstrip())


# TASK 9:  Ask a user to enter a sentence and print the number of vowels in it
word = input("Kindly enter any sentence of your choice: ")
print(word.count("a"))


# TASK 10: Convert a string "1234" to an integer and multiply it by 2
string = "1234"
integer = int(string)


# TASK 11: Given "apple,banana,orange", split the list into a string of fruits
fruit = "apple, banana, orange"
print(fruit.split())


# TASK 12: Ask the user for a sentence and print each word on new line.
sentence = input("Write down a sentence: ")
split_sentence = sentence.split()
print(*split_sentence, sep='\n')



# TASK 13: Replace all spaces in a string with underscores(_)
string = ("This is a string")
print(string.replace(" ", "_"))


# TASK 14: Count how many times the letter "a" appears in banana
fruite = "banana"
print(fruite.count("a"))


# TASK 15: Check if a string starts with "httsps://"
url = "https://www.publicacademy"
print(url.startswith("https://"))






































































































