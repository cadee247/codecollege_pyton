favourite_movies = ["count down", "Madea", "shrek"]

for movie in favourite_movies:
	proper_title = movie.title()
	print(f"one of my favourite movies: {proper_title}")

empty_list = []
for numbers in range(1, 20):
	empty_list.append(numbers)

print(empty_list)

my_numbers = [1, 2, 3, 4, 5]
for number in my_numbers:
	print(number)
	
print(favourite_movies[0:2])

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple[0:3])


my_list =["apple","banana","cherry"]
my_tuple =("car", "bicycle", "motorcycle")
popped_item = my_list.pop(2)
print(popped_item)

