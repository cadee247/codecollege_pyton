# 7.1 rental car

# car = input("What kind of car would you like? ")

# print(f"Let me see if I can find you a {car.title()}.")

# 7.2 restaurant seating
# party_size = input("How many people are in your dinner party tonight? ")
# party_size = int(party_size)

# if party_size > 8:
#     print("I'm sorry, you'll have to wait for a table.")
# else:
#     print("Your table is ready.")


#     # 7.4 pizza toppings

# prompt = "\nWhat topping would you like on your pizza?"
# prompt += "\nEnter 'quit' when you are finished: "

# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"  I'll add {topping} to your pizza.")
#     else:
#         break

#     # 7.8 deli

# sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I'm working on your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#     print(f"I made a {sandwich} sandwich.")

#     # 7.10 dream vacation

    
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")