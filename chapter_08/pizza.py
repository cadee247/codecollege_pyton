def pizza_oven(*toppings):
    print(f"Here is your pizza with the following toppings: {', '.join(toppings)}.")

pizza_oven("ham", "cheese", "pepper")




def print_multiple_values(*args):
    for value in args:
        print(value)

# Function call with multiple values
print_multiple_values("Alice", 30, "Johannesburg","Developer")


