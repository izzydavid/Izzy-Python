#List Methods 2
basket = [1, 2, 3, 4, 5]  #Searches for what index item is in the list.

print(basket.index(2))

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

print(basket.index('d', 0, 5))

print('d' in basket)
print('i' in 'Hi my name is David')
print(basket.count('d'))