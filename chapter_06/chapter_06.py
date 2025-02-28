from dataclasses import field


my_person = {
  "name":"Cadee",
    "age": 25,
    "language": "Python"
 }

print(my_person)


my_person["gender"] = "female"


print(my_person)

my_person["age"] = 26


print(my_person)

print(my_person["language"])

del my_person["name"]
print(my_person)

my_person.pop("gender")
print(my_person)


my_numbers = {
    "one": 1,
    "two": 2,
    "three": 3
}

print(my_numbers.get("four", "No such key"))

#making a dict with names for keys and programming langs for values
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'Javascript',
 }

#making a for loop that itterates ofver the values of 
#the favorite_languages dict using the .value() dict method
for name in favorite_languages.values():
    #every value will be checked to see if it says js, and when it is it will print forbidden
    if name == "Javascript":
        print("Forbidden...")
    #else it will print the name and noice
    else:
        print(f"{name}, noice")




mom = {
    "name": "Nicky",
    "age" : "30",
    "hometown": "johannesburg"
}

dad = { 
    "name": "Dean",
    "age": "50",
    "hometown": "George"
}

family = [mom, dad]

best_friend = {
    "name": "Akhona",
    "age": "19",
    "hometown": "johanessburg"
}

family.append(best_friend)
print(family)




dad = {
    "name": "Anton",
    "age": 64,
    "hometown": "Johannesburg",
    "hobbies": ["coding", "music"]
}

mom = {
    "name": "Gwen",
    "age": 58,
    "hometown": "Pretoria",
    "hobbies": ["piano", "teaching"]
}

sibling = {
    "name": "Matthew",
    "age": 25,
    "hometown": "George",
    "hobbies": ["gaming", "skating"]
}

family = [dad, mom, sibling]

best_friend = {
    "name": "Rob",
    "age": 28,
    "hometown": "Cape Town",
    "hobbies": ["guitar", "gaming"]
}

family.append(best_friend)

print(family[3]["hobbies"][1])