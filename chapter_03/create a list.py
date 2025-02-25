# names

names = ['siyabonga', 'jesse', 'jade']
print(names)
print(names[0]) 
print(names[1])
print(names[2])

# 3.2)greetings
names = ['siyabonga', 'jesse', 'jade']
message = f"Hello, {names[0].title()}!"
print(message)
message = f"have a fantastic day, {names[1].title()}!"
print(message)
message = f"goodnight, {names[2].title()}!"
print(message)

# 3.3) your own list
cars = ['bmw', 'audi', 'toyota', 'honda', 'ford']
message = f"I would like to own a {cars[0].title()} car."
print(message)  

# 3.4) guest list
guests = ['siyabonga', 'jesse', 'jade']
message = f"Hello, {guests[0].title()}! I would like to invite you to dinner."
print(message)
message = f"Hello, {guests[1].title()}! I would like to invite you to dinner."
print(message)
message = f"Hello, {guests[2].title()}! I would like to invite you to dinner."
print(message)

# 3.5) changing guest list
guests = ['siyabonga', 'jesse', 'jade']     
message = f"Hello, {guests[0].title()}! I would like to invite you to dinner."
print(message)
message = f"Hello, {guests[1].title()}! I would like to invite you to dinner."
print(message)
message = f"Hello, {guests[2].title()}! I would like to invite you to dinner."
print(message)
name = guests[0]
print(f"{name.title()} can't make it to dinner.")
del guests[0]
guests.insert(0, 'james')
message = f"Hello, {guests[0].title()}! I would like to invite you to dinner."
print(message)
name = guests[0].title()
print(f"{name} I would like to invite you to dinner.")
name = guests[1].title()
print(f"{name} I would like to invite you to dinner.")
name = guests[2].title()
print(f"{name} I would like to invite you to dinner.")

# 3.6) more guests
guests = ['siyabonga', 'jesse', 'jade']
message = f"Hello, {guests[0].title()}! I would like to invite you to dinner."
print(message)
message = f"Hello, {guests[1].title()}! I would like to invite you to dinner."
print(message)
message = f"Hello, {guests[2].title()}! I would like to invite you to dinner."
print(message)
name = guests[0]
print(f"{name.title()} can't make it to dinner.")
del guests[0]
guests.insert(0, 'james')
message = f"Hello, {guests[0].title()}! I would like to invite you to dinner."
print(message)
name = guests[0].title()
print(f"{name} I would like to invite you to dinner.")
name = guests[1].title()
print(f"{name} I would like to invite you to dinner.")
name = guests[2].title()
print(f"{name} I would like to invite you to dinner.")
print("I found a bigger table!")
guests.insert(0, 'sarah')
guests.insert(2, 'jason')

name = guests[0].title()
print(f"{name} I would like to invite you to dinner.")
name = guests[1].title()
print(f"{name} I would like to invite you to dinner.")
name = guests[2].title()
print(f"{name} I would like to invite you to dinner.")
name = guests[3].title()
print(f"{name} I would like to invite you to dinner.")
name = guests[4].title()
print(f"{name} I would like to invite you to dinner.")


# 3.7) shrinking guest list
guests = ['siyabonga', 'jesse', 'jade']
message = f"Hello, {guests[0].title()}! I would like to invite you to dinner."
message = f"Hello, {guests[1].title()}! I would like to invite you to dinner."
message = f"Hello, {guests[2].title()}! I would like to invite you to dinner."
message = f"{guests[0].title()} can't make it to dinner."
del guests[0]   
guests.insert(0, 'james')
message = f"Hello, {guests[0].title()}! I would like to invite you to dinner."
message = f"{guests[1].title()} I would like to invite you to dinner."
message = f"{guests[2].title()} I would like to invite you to dinner."
message = f"{guests[0].title()} I would like to invite you to dinner."
message = f"{guests[2].title()} I would like to invite you to dinner."
print("\nSorry, we can only invite two people to dinner.")

# ...existing code...
if guests:
    name = guests.pop()
    print(f"Sorry, {name.title()} there's no room at the table.")

if guests:
    name = guests.pop()
    print(f"Sorry, {name.title()} there's no room at the table.")

if guests:
    name = guests.pop()
    print(f"Sorry, {name.title()} there's no room at the table.")

if guests:
    name = guests.pop()
    print(f"Sorry, {name.title()} there's no room at the table.")

if guests:
    name = guests[0].title()
    print(f"{name}, please come to dinner.")

if len(guests) > 1:
    name = guests[1].title()
    print(f"{name}, please come to dinner.")

if len(guests) > 2:
    del guests[2]

if guests:
    del guests[0]
# ...existing code...

# 3.8) seeing the world