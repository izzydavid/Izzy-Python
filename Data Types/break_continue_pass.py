# Break, Continue, Pass

# Pass
my_list = [1, 2, 3]
for item in my_list:
    # thinking about it
    pass

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass

# Break
my_list = [1, 2, 3]
for item in my_list:
    print(item)
    break

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break

# Continue
my_list = [1, 2, 3]
for item in my_list:
    print(item)
    continue

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue
