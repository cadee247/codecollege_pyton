# username = input("what is your name? ")
# passions_one = input("What is your first passion? ")
# passions_two = input("What is your second passion? ")
# passions_three = input("What is your third passion? ")
# my_passions = [passions_one, passions_two, passions_three]

# print(f"Welcome to your python code {username}./nHere is a list of your passions:/npassion one:{my_passions[1]} ")


# age = input("How old are you? ")
# age = int(age)

# if age >= 18:
#     print("Go watch SAW")
# elif age <= 18:
#     print("Watch a diffrent movie")


# always_true = True
# while always_true == True:
#     print("boom")


import random  # Import the random module for generating random choices

characters = ["Alice", "Bob", "Charlie"]  # List of characters
actions = ["dances", "sings", "jumps"]  # List of actions
places = ["on a mountain", "in a castle", "under the sea"]  # List of places

count = 0  # Initialize the counter
while count < 1:  # Loop runs once as long as count is less than 1
    character = random.choice(characters)  # Pick a random character
    action = random.choice(actions)  # Pick a random action
    place = random.choice(places)  # Pick a random place
    
    print(f"{character} {action} {place}.")  # Print the generated sentence
    
    count += 1  # Increment the counter to end the loop



        
    