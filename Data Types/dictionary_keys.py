# Dictionary Keys
# Dictionary key value needs to be immutable, dictionary key will not accept mutable values.
dictionary = {
    '123': [1, 2, 3],
    '123': 'hello',
}
# List does not work as a dictionary key because it's not an immutable value.
print(dictionary['123'])
