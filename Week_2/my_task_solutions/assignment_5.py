# # TASK 1: Create and Display
# dish_1 = input("Enter one of your favourite dishes: ")
# dish_2 = input("Enter another one of your favourite dishes: ")
# dish_3 = input("Enter  one other  favourite dish of yours: ")
# dish_tuple = (dish_1, dish_2, dish_3)
# print(tuple(dish_tuple))
# print(f"{dish_1}\n{dish_2}\n{dish_3}")


# TASK 2: Tuple and Input
# friend_name = input("Give me the name of your five best friends. Kindly separate them with commas: ")
# split_friends = friend_name.split()
# friends = tuple(split_friends)
# print(friends[::-1])



# # TASK 3: Tuple Operations
# state_name = (input("Enter any five states that you know. Please separate them by commas: "))
# split_state = state_name.split(',')
# tuple_state = tuple(split_state)
# print(tuple_state[0::4])
# print("lagos" in tuple_state)
# print(len(tuple_state))

# TASK 4: Tuple Unpacking
# FName = input("What is your first name please?: ")
# age = int(input("How old are you?: "))
# fav_color = input("What is your favourite color?: ")
# home_town = input("Where is your home town?")
# profile = FName, age, fav_color, home_town
# tuple_profile = tuple(profile)
# print(f"Name: \t\t\t{FName}\nAge: \t\t\t{age}\nFavourite Color:\t{fav_color}\nHome Town:\t\t{home_town}")

# # TASK 5: Modify Tuple Indirectly
# item_list = list(input("Kindly enter three items you would like to buy. Please use space and commas: "))
# shopping_list = list(item_list)
# tuple_shopping_list = tuple(shopping_list)
# updated_list = item_list + tuple_shopping_list
# print(updated_list)

# # TASK 1: Create and Display
item_1 = input("Enter your first item: ")
item_2 = input("Enter your second item: ")
item_3 = input("Enter  your third item: ")
lists = tuple(item_1 + item_2 + item_3)
shopping_list = list(lists.split(','))

item_4 = shopping_list.append(input("Enter another item"))
item_5 = shopping_list.append(input("Enter your fifth item"))
tuple_list = tuple(shopping_list)
print(shopping_list)




# TASK 6























































