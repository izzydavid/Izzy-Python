# Parameters and Arguments
# Default Parameters

# Parameters 
def say_hello(name ='Darth Vader', emoji = '👿'): 
  print(f'hellllooooo {name} {emoji}')

# Positional Arguments 
say_hello('Andrei', '😀')
say_hello('Dan', '😀')
say_hello('Emily', '😀')

# Keyword arguments
say_hello(emoji = '😀', name = 'bibi')
say_hello()