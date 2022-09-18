#Password Checker
input('jayjay')
input('secret')

print('{username}, password {******} is {6} is long')

print('*' * 10)

#Password Checker Exercise
username = input('What is your username?')
password = input('What is your password?')

password_length = len(password)
hidden_password = '*' * password_length

print(
    f'{username}, your password {hidden_password} is {password_length} characters long!'
)

print('*' * 10)
