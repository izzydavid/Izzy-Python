# Sets 2
my_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# .difference()
print(my_set.difference(your_set))
# The difference your_set from the my_set point of view is 1,2,3, it informs the user.

# # .discard()
print(my_set.discard(5))
print(my_set)

# # .difference_update()
print(my_set.difference_update(your_set))
print(my_set)

# .intersection()
print(my_set.intersection(your_set))

# .isdisjoint()
print(my_set.isdisjoint(your_set))
# Disjointed means these sets have nothing in common.

# .issubset()
print(my_set.issubset(your_set))
# Is my_set with {4,5} a subset of your_set {4,5,6,7,8,9,10}

# .issuperset()
print(your_set.issuperset(my_set))
# Does my_set encompases your_set? False. Your_set encompases my_set? True.

# .uion()
print(my_set.union(your_set))
print(my_set | your_set)  #Shortcut to the Union set method.
# Unites the sets together and removes duplicates, created a new set for the user.
