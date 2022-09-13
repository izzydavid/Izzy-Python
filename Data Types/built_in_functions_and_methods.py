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
