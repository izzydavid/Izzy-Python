#List methods
basket = [1, 2, 3, 4, 5]
print(len(basket))

#adding
basket.append(100)  # adds 100 to the end of the variable

# Append changes the list inplace of the variable basket. It is only adding 100 to this basket you gave me. It is not producing a value, just changing the result.

basket.insert(4, 100)  # Inserts 100 at the 4th index.
basket.extend([100, 101])  # iterable, adds 100 and 101 to the end of the list.

new_list = basket
print(basket)
print(new_list)  # Outputs none

#removing
basket.pop()  # Pops off the value at the end of the list
basket.pop()
basket.pop(0)
print(basket)

basket.remove(4)
print(basket)

new_list = basket.pop(4)  # Pop returns whatever you just removed.
print(new_list)

new_list = basket.clear()  # Removes the list and clears
print(basket)
