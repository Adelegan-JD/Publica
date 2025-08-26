# # CONTROL FLOW IN PYTHON

# # Control flowas refers to the order in which statements are executed in a program. Instead of always running line by line, control flow allows a program to make decisions, repeat actions and exit or skip parts of code.
# # Control flow is the foundation for logic and problem solving in programming.
# # Control flow is divided into three parts:

# # 1. CONDITIONAL STATEMENTS
# # if statements: It executes a block only when a condition is true

# age = 20
# if age >= 18:
#     print("You are eligible to vote")

#  # Use cases of "if" conditions are: checking for eligibility, validating login attempts, ensuring a minimum purchase requirement, etc  


# # 2. if/else statements: It provides two alternative paths

# wallet = 400
# price = 500

# if wallet >= price:
#     print("Purchase successful")
# else:
#     print("Insufficient balance")

# # Use cases of if/else statements include: deciding success or failure of a payment,  granting or denying access to a system, determining pass/fail in an exam, etc


# # 3. if-elif-else statements: They are used for multiple conditions

# score = 85
# if score >= 70:
#     print("Grade A")
# elif score >= 50:
#     print("Grade B")
# else:
#     print("Grade C")

# # Some use cases of this are: student grading systems, assigning ticket categories(VIP, Regular, Student), categorizing temperatures(hot, warm, cold), etc


# # 4. Nested if: This is when you place an if statment inside another if statement
# age = 19
# citizen = True

# if age >= 18:
#     if citizen:
#         print("You can vote")
#     else: 
#         print("You must be a citizen to vote")
# else: 
#     print("Too young to vote")

# # Some use cases of this are: voting eligibility(age + citizenship), banking(account active + balance sufficient), school admission (age + gade level)


# # LOOPS
# # 1. FOR LOOPS: This is used for iterating over a sequence(strings, list, tuples, dictionaries)

# # Iterating through a STRING(sequences of character). Some use cases include counting vowels/consonants, password validation(checking digits/special characters), text analysis, etc

# word = "PYTHON"
# for char in word:
#     print(char)

# #Iterating through each element in a LIST. Some usecases are: iterating through shopping lists, checking availability of products, displaying student names, etc

# fruits = ["apple", 'banana', 'orange']
# for fruit in fruits:
#     print(f"I like {fruit}")

# # Iterating through elements in a TUPLE. This works like lists, just that they are immutable
# # Some use cases of this are: storeing fixed sensor readings, displaying fixed seating positions, etc
# coordinates = (0.4573, -9.3558748, 3.87585)
# for point in coordinates:
#     print(f"Point: {point}")


# # Iterating through each element in a DICTIONARY. Some common use cases are: reading database records, showing user profile details, checking configuration settings, etc

# student = {"Name": "Tunde", "Age": 16, "Grade": "A"}
# for key, value in student.items():
#     print(f"{key}: {value}")



# # 2. WHILE LOOPS: This is used to repeatedly execute a block of code as long as a given condition is true. Unlike the "for loop" (which iterates over sequences like lists, tuples, etc), the while loop is condition-based.
# # The code block of while condition is :
# # The condition must evaluate to "True" for the loop to continue running
# # When the condition becomes "False", the loop stops

# # Using while loop,

# # Example 1:
# # Let the loop start with count = 1
# # Let it keep printing until count is greater than 5
# # # Let the loop terminate when the condition is no longer True

# count = 1
# while count <= 5:
#     print("Number:", count)
#     count += 1

# # Incrementing with while

# num = 1
# while num <= 10:
#     print(num, end=" ")
#     num += 1

# # Decrementing with while

# timer = 10
# while timer > 0:
#     print("Countdown: ", timer)
#     timer -= 1

# # while with user input
# # Keep asking until the user enters a correct password.

# password = " "
# while password != "python123":
#     password = input("Enter the password: ")

# print("Access Granted")



# # Understanding While True
# # A while loop must include a break statementt to stop

# # Keep asking the user for a name until they type "exit"
# while True:
#     name = input("Enter your name (type 'exit' to quit):")
#     if name.lower() == "exit":
#         print("Goodbye!")
#         break
#     print(f"Hello, {name}")



# # LOOP CONTROL STATEMENTS (Break, Continue, and Pass)

# # These keywords help us control the behaviour of loops(for and while).
# # Instead of loops always running all iterations, we can skip steps, 
# # stop early, or do nothing intentionally

# # 1. break: This stops loop immediately. It is used if a condition is met and there's no need to continue looping

# for num in range(1, 11):
#     if num == 5:
#         break
#     print(num)
# # The loop starts counting from one to ten. It stops completely when num == 5. 
# # The "break" makes the loop stop searching when an item is found. It exits when user input matches a condition. It prevents unncessary iterations.


# # 2. continue: This skips the current iteration and moves to the next one. It is used if you want toignore some values but keep the loop running
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# 3 is skipped, but the loop continues. 
# Some use cases include: skipping invalid data, ignore unwanted characters(like spaces in a string), continue running bu avoid certain casees, etc


# 3. pass: This does nothing. It serves as a placeholder to avoid errors. It is used if the final code hasn't been written yet but you want to keep the structure

for num in range(1, 6):
    if num == 3:
        pass
    else: 
        print(num)








