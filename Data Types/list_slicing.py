#List slicing as lists are mutable and creating a new copy of the list when slicing.
string = 'helllooo'
string[0:2:1]

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'

print(amazon_cart[0:3])

new_cart = amazon_cart[:]  # Copy the entire list with list slicing
new_cart[0] = 'gum'

print(new_cart)
print(amazon_cart)
