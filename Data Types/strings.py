#String data type 'str' is a data type
print(type("Hi Hello there 24!"))

username = 'supercoder'
password = 'supersecret'

#Example of a long string is 3 quotes " ''' '" to save in memory a value like a paragraph. Similar to back "`" tick literals in javascripts.
long_string = '''
WOW
O O 
---
'''
print(long_string)
first_name = 'David'
last_name = 'Irizarry'
full_name = first_name + ' ' + last_name
print(full_name)

#String concatenation
print('hello ' + 'David')

#Example of how you cannot conduct string concatenation with an integer data type.
# print('hello ' + 5)

#Type Coversion.

#Example reads the statement in the following order of operation (100 -> str -> int -> type).
print(type(int(str(100))))

#Second example of the order of operations or operation precedence.
a = str(100)
b = int(a)
c = type(b)
print(c)

#Escape Sequences. Backslash "\" within a string denotes to python that the following should be treated as a string.

#Backslash combined with the letter n, '\n' is executing a new line after the '\n' of a string.

#Backslash combined with with the letter t, '\t' is executing a "new tab" after '\n' of a string.
weather = "\t It\'s \"kind of\" sunny \n hope you have a good day"
print(weather)

#Formatted strings
name = 'Johnny'
age = 55
print('Hi ' + name + '. You are ' + str(age) + ' years old')

#Example of a new feautre in python 3, when a user adds 'f' at the start of their string it denotes the following is a formatted string.
print(f'hi {name}. You are {age} years old')

#Example in python 2, when user adds '{}' to place their values within a string and use .format('Johnny', '55')) to print out the same statement.
print('hi {}. You are {} years old'.format('Johnny', '55'))

#Example with variables and formatted strings in python 2.
print('hi {}. You are {} years old'.format(name, age))

#Example of a formatted string with new variables stored in python 2.
print('hi {new_name}. You are {age} years old'.format(new_name='sally',
                                                      age=100))
