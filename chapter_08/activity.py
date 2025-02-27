# def display_message():
#     """Display a message about what I'm learning."""
#     msg = "I'm learning to store code in functions."
#     print(msg)

# display_message()




# # 8.2) favourite_book.py

# def favorite_book(title):
#     """Display a message about someone's favorite book."""
#     print(f"{title} is one of my favorite books.")

# favorite_book('The Abstract Wild')

# 8.5) cities.py

# def describe_city(city, country='the United States'):
#     msg = f"{city.title()} is in {country.title()}."
#     print(msg)

# describe_city('new york city')
# describe_city('califonia')
# describe_city('las vegas')

# # 8.6) city_names.py
# def city_names(city, country):
#     return f"{city.title()}, {country.title()}"

# city = city_names('johanessburg', 'south africa')
# print(city)

# city = city_names('cape town', 'south africa')
# print(city)

# city = city_names('tokyo', 'japan')
# print(city)

# # 8.12) sandwich.py
# def make_sandwich(*items):
#     """Make a sandwich with the given items."""
#     print("\nI'll make you a great sandwich:")
#     for item in items:
#         print(f"  ...adding {item} to your sandwich.")
#     print("Your sandwich is ready!")

# make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
# make_sandwich('turkey', 'apple slices', 'honey mustard')
# make_sandwich('peanut butter', 'strawberry jam')