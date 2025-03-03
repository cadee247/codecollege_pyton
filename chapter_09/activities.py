# class Restaurant: #9.1Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.

# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods
#     """A class representing a restaurant."""

#     def __init__(self, name, cuisine_type):
#         """Initialize the restaurant."""
#         self.name = name.title()
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         """Display a summary of the restaurant."""
#         msg = f"{self.name} serves wonderful {self.cuisine_type}."
#         print(f"\n{msg}")

#     def open_restaurant(self):
#         """Display a message that the restaurant is open."""
#         msg = f"{self.name} is open. Come on in!"
#         print(f"\n{msg}")

# restaurant = Restaurant('the mean queen', 'pizza')
# print(restaurant.name)
# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

#9.6An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a
#  list of ice cream flavors. Write a method that displays theese flavors. Create an instance of IceCreamStand, and call this method.
# class Restaurant:
#     """A class representing a restaurant."""

#     def __init__(self, name, cuisine_type):
#         """Initialize the restaurant."""
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """Display a summary of the restaurant."""
#         msg = f"{self.name} serves wonderful {self.cuisine_type}."
#         print(f"\n{msg}")

#     def open_restaurant(self):
#         """Display a message that the restaurant is open."""
#         msg = f"{self.name} is open. Come on in!"
#         print(f"\n{msg}")

#     def set_number_served(self, number_served):
#         """Allow user to set the number of customers that have been served."""
#         self.number_served = number_served

#     def increment_number_served(self, additional_served):
#         """Allow user to increment the number of customers served."""
#         self.number_served += additional_served


# class IceCreamStand(Restaurant):
#     """Represent an ice cream stand."""

#     def __init__(self, name, cuisine_type='ice cream'):
#         """Initialize an ice cream stand."""
#         super().__init__(name, cuisine_type)
#         self.flavors = []

#     def show_flavors(self):
#         """Display the flavors available."""
#         print("\nWe have the following flavors available:")
#         for flavor in self.flavors:
#             print(f"- {flavor.title()}")


# big_one = IceCreamStand('The Big One')
# big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

# big_one.describe_restaurant()
# big_one.show_flavors()


#9.14Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the
#  list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
# from random import choice

# possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# winning_ticket = []
# print("Let's see what the winning ticket is...")

# # We don't want to repeat winning numbers or letters, so we'll use a
# #   while loop.
# while len(winning_ticket) < 4:
#     pulled_item = choice(possibilities)

#     # Only add the pulled item to the winning ticket if it hasn't
#     #   already been pulled.
#     if pulled_item not in winning_ticket:
#         print(f"  We pulled a {pulled_item}!")
#         winning_ticket.append(pulled_item)

# print(f"\nThe final winning ticket is: {winning_ticket}")




#9.15You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins.
#  Print a message reporting how many times the loop had to run to give you a winning ticket.

from random import choice

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a
    #   while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the 
    #   winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")