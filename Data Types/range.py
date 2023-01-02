# Range

# Range is a function object returns an object that produces a sequence of integers from start to stop.

# Iterates over the sequence of numbers between 0 through 100 and prints out the number 0 to 100.
for number in range(0, 100):
    print(number)

# Iterates over the sequence of numbers between 0 through 10 and prints out 'email email list' ten times.
for number in range(0, 10):
    print('email email list')

# Iterates over the sequence of 0 through 10 every two numbers.
for _ in range(0, 10, 2):
    print(_)

# Iterates over the sequence of 10 to 0 in reverse order, listing each sequence of number from 10 to 0. Does not work if stated (0, 10, -1).
for _ in range(10, 0, -1):
    print(_)

# Iterates over the sequence of 10 to 0 in reverse order and by every two numbers, listing each sequence of number from 10 to 0.
for _ in range(10, 0, -2):
    print(_)

for _ in range(10, 0, -2):
    print(list(range(10)))
