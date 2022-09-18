# Tuples
# Tuple(s) are like lists but not like lists, because we cannot modify a tuple.
# Benefits of a tuple is to notify other developers that these items should not and will not change. Cannot sort or reverse a tuple, slightly faster than a list.
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[1] = 'z'
# print(my_tuple[1])
print(5 in my_tuple)
# user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
# print(user.items())

user = {(1, 2): [1, 2, 3], 'greet': 'hello', 'age': 20}
print(user[(1, 2)])
