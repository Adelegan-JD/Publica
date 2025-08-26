# Task 1: Your favourite life quote
# quote = input("What is your favourite quote?: ")
# title_quote = quote.title()
# print(f'\"{title_quote}\"')

      

# TASK 2: Shopping List Manager
# empty_list = []
# item1 = input("What is the first item you would like to buy?: ")
# item2 = input("What is the second item you would like to buy?: ")
# item3 = input("What is the third item you would like to buy?: ")
# empty_list.append(item1)
# empty_list.append(item2)
# empty_list.append(item3)
# print(empty_list)

# # TASK 3: Word Counter
sentence = input("Kindly a choice sentence of yours: ")
split_sentence = sentence.split()
print(len(split_sentence))

# # TASK 4: Name Organizer
# name = input("Enter five names of your choice, and please separate them by space: ")
# lower_name = name.lower()
# sorted_name = name.sort()
# listed_name = list()

# TASK 5: Student Record Tracker
name_list = []
score_list = []

# Collect student names
name1 = input("Kindly enter the name of the first student: ")
name2 = input("Kindly enter the name of the second student: ")
name3 = input("Kindly enter the name of the third student: ")

# Collect student scores
score1 = int(input("What is the score of the first student?"))
score2 = int(input("What is the score of the second student?"))
score3 = int(input("What is the score of the third student?"))

# Append student names
name_list.append(name1)
name_list.append(name2)
name_list.append(name3)

# Append student scores
score_list.append(score1)
score_list.append(score1)
score_list.append(score1)

# Print formatted output
print(f"Name\tScore\n{name_list[0]}\t{score_list[0]}\n{name_list[1]}\t{score_list[1]}\n{name_list[2]}\t{score_list[2]}")


# TASK 6: Word Analyzer
word = input("Kindly enter a sentence: ")
print(len(word))
print(word.isupper())
print(word.islower())
print(word.istitle())
print(word[::-1])



# TASK 7: List Manipulation
# Create a list of cities
cities = ["Abuja", "Kano", "New York", "Ibadan", "Ogbomoso"]

# Change the third city into a new one entered by the user
cities[2] = input("Enter a new city: ")

# Remove the last city
cities.pop()

# Insert a new city as the first one
cities.insert(0, input("Enter a new city"))

# Print the updated list
print(cities)






























































