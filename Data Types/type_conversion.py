#Type Coversion 1.

#Example reads the statement in the following order of operation (100 -> str -> int -> type).
print(type(int(str(100))))

#Second example of the order of operations or operation precedence.
a = str(100)
b = int(a)
c = type(b)
print(c)
