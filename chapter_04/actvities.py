favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Print the names of all the pizzas.
for pizza in favorite_pizzas:
    print(pizza)

print("\n")

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print(f"I really love {pizza} pizza!")

print("\nI really love pizza!")

# # 4.2)animals
# animals = ["spider monkey", "lemur", "giraffe"]

# # Print each animal.
# for animal in animals:
#     print(animal)

# print("\n")

# # Print a statement about each animal.
# for animal in animals:
#     print(f"A {animal} has a long tail.")

# print("\nAll of these animals have long tails.")

# 4.3)numbers
numbers = list(range(1, 21))

for number in numbers:
    print(number)

    # 4.5)summing a million
    numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# # 4.6)odd numbers
# odd_numbers = list(range(1, 20, 2))

# for number in odd_numbers:
#     print(number)

# 4.7)threes
threes = list(range(3, 31, 3))

for number in threes:
    print(number)

# 4.8)cubes
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

# # 4.9)cube comprehension
# cubes = [number**3 for number in range(1,11)]

# for cube in cubes:
#     print(cube)

# 4.10)Slices
slices = list(range(1, 11))
print(slices[1:3])
print(slices[3:6])


# 4.11)My pizzas, your pizzas
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")

# 4.12)More loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")

# 4.13)Buffet
menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )

print("You can choose from the following menu items:")
for item in menu_items:
    print(f"- {item}")

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print(f"- {item}")

# 4.14)Pizzas