# # 6.1) person
# person = {
#     'first_name': 'eric',
#     'last_name': 'matthes',
#     'age': 43,
#     'city': 'sitka',
#     }

# print(person['first_name'])
# print(person['last_name'])
# print(person['age'])
# print(person['city'])

# # 6.3) glossary
# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     }

# word = 'string'
# print(f"\n{word.title()}: {glossary[word]}")

# word = 'comment'
# print(f"\n{word.title()}: {glossary[word]}")

# word = 'list'
# print(f"\n{word.title()}: {glossary[word]}")

# word = 'loop'
# print(f"\n{word.title()}: {glossary[word]}")

# word = 'dictionary'
# print(f"\n{word.title()}: {glossary[word]}")



# # 6.4) glossary 2
# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     'key': 'The first item in a key-value pair in a dictionary.',
#     'value': 'An item associated with a key in a dictionary.',
#     'conditional test': 'A comparison between two values.',
#     'float': 'A numerical value with a decimal component.',
#     'boolean expression': 'An expression that evaluates to True or False.',
#     }

# for word, definition in glossary.items():
#     print(f"\n{word.title()}: {definition}")


#     # 6.5) rivers
    
# rivers = {
#     'nile': 'egypt',
#     'mississippi': 'united states',
#     'fraser': 'canada',
#     'kuskokwim': 'alaska',
#     'yangtze': 'china',
#     }

# for river, country in rivers.items():
#     print(f"The {river.title()} flows through {country.title()}.")

# print("\nThe following rivers are included in this data set:")
# for river in rivers.keys():
#     print(f"- {river.title()}")

# print("\nThe following countries are included in this data set:")
# for country in rivers.values():
#     print(f"- {country.title()}")

    # 6.8) pets
#      Make an empty list to store the pets in.
# pets = []

# Make individual pets, and store each one in the list.
pets = []

# Adding pets to the list
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Displaying information about each pet
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
