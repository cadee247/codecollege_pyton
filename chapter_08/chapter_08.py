

def my_name(user, age, nation = "South Africa"):
	print(f"Welcome back {user}! it must be nice to be {age} years old... a proud {nation} citizen")

my_name(input("May i have your name please: "), input("How old are you: "))



# def compare_numbers(a, b):
#     if a > b:
#         return "a is greater"
#     else:
#         return "a is not greater"


# result = compare_numbers(3, 2) 
# print(result)

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)
my_list = [1, 2, 3, 4, 5]

copied_list = None

def my_test_function(list):
    copied_list = list.reverse()
    return copied_list
    print(list)

my_test_function(my_list[:])

print(my_list)
print(copied_list)