#How to create a variable and print the value of the variable. Assigning a value to a variable is also called binding.
iq = 190
print(iq)

#Variable are snake_case, start with lowercase or underscore, letters, numbers, underscores, case sensitive, and cannot overwrite keywords.

#Example of snake_case
user_iq = 190
print(iq)

#Example of snake_case with a private varaible
_user_iq = 190
print(_user_iq)

#Example of case sensitive varaiable.
# user_IQ = 190
# print(user_iq)

#Example of why you cannot overwrite keywords which already are defined
# print = 190
# print(print)

#A variable should be a good descriptor or indicator of what the variable is used/stored for in their code.

#Example of how to store and use variables and Arithmetic operators.
iq = 190
user_age = iq / 4
a = user_age
print(a)

#Constants is a type of variable which doesn't change or meant to change.
PI = 3.14
print(a)

#Dunder is another type of variable and should be left alone. A user knows if something is a "dunder" variable when there are two underscores.
# __

#Example of assigning multiple variables to a value.
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

#Expression & Statements.

#Example of expression is a piece of code which produces a value (e.g. iq/5) is the expression.
iq = 100
user_age = iq / 5
print(user_age)

# Example of a statement. A statement is an entire line of code (e.g. user_age = iq / 5) & (iq = 100) is the statement.
iq = 100
user_age = iq / 5
print(user_age)

#Augemented assignment operator.

#Example of how we can use a assignment operator to redefine the value of a variable (e.g. some_value = +=2). This will take the declared variable and add 2. If you don't declare the variable first then you cannot conduct an augemented assignment operator.
some_value = 5
print(some_value)
some_value += 2
print(some_value)
some_value -= 2
print(some_value)
some_value *= 2
print(some_value)
some_value = some_value * 2
print(some_value)

# Instead of int or float
# Complex Data Type
# Binary Numbers can be returned through bin
print(bin(5))
print(int('0b101', 2))

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

#Type Coversion 1.

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
print('hi {new_name}. You are {age} years old'.format(new_name='Sally',
                                                      age=100))

#Example of string indexes, where you are asking the computer to graph the first variable of selfish which is "m"

selfish = 'me me me'
# 01234567
print(selfish[0])

selfish = '01234567'
# 01234567
print(selfish[0])

#Start and Stop default is one by one iteration over a number
selfish = '01234567'
# 01234567
# [start:stop]
print(selfish[0:8])

#Stepover can hopover a # of iterations specified
selfish = '01234567'
# 01234567
# [start:stop:stepover]
print(selfish[0:8:2])

#Start at 1 and stop when there is nothing else there.
selfish = '01234567'
# 01234567
# [start:stop:stepover]
print(selfish[1:])

#Start at default 0 and goes to 5.
selfish = '01234567'
# 01234567
#[start:stop]
print(selfish[:5])

#Start at default 0, ends whenever string ends and stepping over it once.
selfish = '01234567'
#01234567
#[start:stop:stepover]
print(selfish[::1])

#Start at the end of the string when using the negative index number.
selfish = '01234567'
#01234567
#[start:stop:stepover]
print(selfish[-2])

#Start and stop and index from the back, which provides the reverse output of the string index.
selfish = '01234567'
#01234567
#[start:stop:stepover]
print(selfish[::-1])  # common method to reverse the order of a string

#Strings in python cannot be changed also known as immutability, the value of a string can be re-assigned.
selfish = '01234567'
#  01234567
selfish = selfish + '8'

print(selfish)

#Built-in Functions, following are examples of built-in functions.

# str()
# int()
# print()
print(len('hellloooo'))  # len() calculates the length

greet = 'hellloooo'
print(greet[:])
print(greet[0:len(greet)])

#Built-in Methods
quote = 'to be or not to be'
print(quote.upper())  # Upper will uppercase the entire string
print(quote.capitalize())  # Capitalize will capitalize the string
print(quote.lower())  # Lower will lower the case of the string
print(quote.find('be'))  # Find will find the first occurence
print(quote.replace('be', 'me'))  # Replaces all occurences of be with me
quote = 'to be or not to be'  #Stays immutable
quote2 = quote.replace('be', 'me')
print(quote2)
print(quote)

#Booleans can be True or False, their value is 0 and 1.
name = 'David'
is_cool = False

is_cool = True

print(bool(1))
print(bool(0))
print(bool('True'))
print(bool('False'))

#Type conversion 2
name = 'David'
age = '36'
relationship_status = 'single'
relationship_status = 'it\'s complicated'
print(relationship_status)
birth_year = input('What year were you born?')
print(type(birth_year))
age = 2022 - int(birth_year)
print(f'your age is: {age}')
