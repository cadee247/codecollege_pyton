# function = A block of reusable code 
#   place () after the function name to invoke it
def happy_birthday():

  print("Happy birthday to you!")
  print(f"ÿou are age years old!")
  print("Happy birthday to you!")
  print()

happy_birthday()

# adding parameters

# def happy_birthday(name, age):
#     print(f"Happy birthday to you, {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()

# happy_birthday("kimmy", 30)
# happy_birthday("jesse", 24)
# happy_birthday("johnathan", 20)



def family_tree(grandmother, mother, daughter):
    print(f"who is the grandmother?{grandmother}")
    print(f"who is the mother?{mother} and who is the daughter?{daughter}")

family_tree("maaleen", "nicky", "cadee")
    

    # return = statement used to end a function 
    #         and sends a result back to the caller

def add(x,y):
   z = x + y 
   return z

def subtract(x,y):
    z = x - y
    return z


def multiply(x,y):
    z = x * y
    return z


def divide(x,y):
    z = x / y
    return z

print(add(1, 2))

print(subtract(1, 2))


print(multiply(1, 2))

print(divide(1, 2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name =  create_name("bro", "code")

print(full_name)

def add_fixed(a, b):
    k = a + b
    return k

def subtract_fixed(a, b):
    k = a - b
    return k

print(add_fixed(100, 150))  # Corrected to pass two arguments
print(subtract_fixed(100, 150))  # Corrected to pass two arguments
