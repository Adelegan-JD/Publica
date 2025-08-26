# TASK 1: Fruit Collector


# Solution
# Step 1: Ask the user to input five choice fruits
# Step 2: Split the fruits
# Step 3: Store the spit fruits into a set

# fruits = input("Kindly enter five fruits of your choice: ")
# split_fruits = fruits.split()
# fruits_list = set(split_fruits)
# print(fruits_list)



# TASK 2: Unique Name Collector

# Solution
# Step 1: create an empty set
# Step 2: Ask the attendees to input their names, and add it to the set
# Step 3: Sort the set list in an alphabetical order

# attendee_list = set()
# attendee_list.add(input("Kindly input your name if you attended the programme: "))
# attendee_list.add(input("Kindly input your name if you attended the programme: "))
# attendee_list.add(input("Kindly input your name if you attended the programme: "))
# attendee_list.add(input("Kindly input your name if you attended the programme: "))
# print("The names of people who attended the seminar are: ", sorted(attendee_list))



# TASK 3: Simulate a football match ticket
# Step 1: Store the seat numbers 1- 50 in a set using the range
# Step 2: Ask users to book a seat by selecting any number between 1 and 50
# Step 3: Use the remove method to remove the selected number
# Step 4: Print the remaining numbers

# ticket_number = set(range(1, 51))
# user_number  = int(input("Kindly book a seat number to watch the football match. \nSelect any number between 1 and 50: "))
# remaining_ticket = ticket_number.remove(user_number)
# print(ticket_number)



# TASK 4: Create a unique Voter's Registration System

# # Create an empty set
voters_list = set()

# Accept first voter's name
voter1 = input("Kindly input your name for the registration: ")
voters_list.add(voter1)

# Accept second voter's name and ensure it's not the same as the first
voter2 = input("Kindly input your name for the registration: ")
if voter2 == voter1:
    print(f"Warning: {voter2} is in the registration file. You have previously registered.")
else:voters_list.add(voter2)

# Accept third voter's name and ensure it's not the same as the second
voter3 = input("Kindly input your name for the registration: ")
if voter3 == voter2 and voter3 == voter1:
    print(f"Warning: {voter3} is in the registration file. You have previously registered.")
else:voters_list.add(voter3)

# Accept fourth voter's name and ensure it's not the same as the first, second and third
voter4 = input("Kindly input your name for the registration: ")
if voter4 == voter1 and voter4 ==2 and voter1 == voter3:
    print(f"Warning: {voter4} is in the registration file. You have previously registered.")
else:voters_list.add(voter4)

print(f"The number of the registered voters is: {len(voters_list)}")








































































































































