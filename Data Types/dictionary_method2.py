# Dictionary Methods 2
user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}

# print('basket' in user) # Searches for 'basket' in the dictionary within user
# print('age' in user.keys()) # Searches for 'age' within the dictionary keys within user.
# print(user.items()) # Returns the key and values in the dictionary, mentioned tuple.
# user.clear()
# user2 = user.copy() # Creates a copy of the dictionary.
# print(user.clear()) # Removes the key/value pair from the user dictionary/object.
# print(user2)
# print(user.pop('age')) # Removes the key referred to as 'age' and returns the 'age' value
# print(user.popitem()) # Remove the last key:value pair that was inserted into the dictionary.
# print(user)
print(user.update({'ages': 55})) # Update method updates a key:value pair that either exist or does not exist in dictionary.
print(user)
