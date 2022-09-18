# Tuples 2
# x,y,z, *other = (1, 2, 3, 4, 5)
# new_tuple = my_tuple[1:2]
# A tuple with a single item typically had a common at the end.
# x = my_tuple[0]
# y = my_tuple[1]

# print(x)
# print(y)
# print(z)
# print(other) # The tuple becomes a list with the *other method.
my_tuple = (1, 2, 3, 4, 5, 5)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))
