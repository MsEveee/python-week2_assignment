# Create an empty list called my_list.
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Inserting the value 15 at the second position in the list.
my_list.insert(1, 15)
print(my_list)

# Extend my_list with another list: [50, 60, 70]
my_list2 = [60, 50, 70]

my_list.extend(my_list2)
print(my_list)

# Remove the last element from my_list.
my_list.pop(-1)
print(my_list)

# Sort my_list in ascending order.
my_list.sort()
print(my_list)


# # Find and print the index of the value 30 in my_list.
index_of_value30 = my_list.index(30)
print(index_of_value30)




