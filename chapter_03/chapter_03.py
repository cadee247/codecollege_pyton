import numbers


my_list =["item1","item2","item3"]


print(my_list)
# my_list = ['Cadee','Mieke','Courtney','Sibusiso','Ronny','Tom','Ulrich','Lindo','Ethan','Lindo','Phumello','Mavelous']
# print(my_list[5])

my_list.append(5)
my_list.append(4)
my_list.insert(4, "Cadee")

del my_list[0]
number_4 = my_list.pop()
my_list.pop()



print(my_list)
print(number_4)

new_list = [1, 2, 3, 4, 5, "billy"]
new_list.remove("billy")
print(new_list)


