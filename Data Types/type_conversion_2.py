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
