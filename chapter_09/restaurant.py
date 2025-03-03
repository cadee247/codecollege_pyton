# class Restaurant:
# 	"""Simple restaurant class"""
	
# 	def __init__(self, restaurant_name, cuisine_type):
# 		"""Initialize name and type"""
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type

# 	def describe_restaurant(self):
# 		"""Describes a restaurant"""
# 		print(f"The restaurant is called {self.restaurant_name}")
# 		print(f"The cuisine type is {self.cuisine_type}")

# 	def open_restaurant(self):
# 		"""Prints open message"""
# 		print(f"The restaurant {self.restaurant_name} is open!")

# Chinese_restaurant = Restaurant("Beijing Temple", "Chinese")
# Mzansi_restaurant = Restaurant("kWA'MAIMAI", "Shisa'nyama")
# American_restaurant = Restaurant("Pitstop", "American")

# Chinese_restaurant.describe_restaurant()
# print("----")
# Mzansi_restaurant.describe_restaurant()
# print("----")
# American_restaurant.describe_restaurant()



class Restaurant:
	def __init__(self, name, cuisine_type):
		self.restaurant_name = name.lower().title().strip()
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"The restaurant is called {self.restaurant_name}")

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name} is open!")

nobu = Restaurant("Nobu", "Asian Fusion")
	
nobu.describe_restaurant()
nobu.open_restaurant()