username = input('Enter your username:  ')
password = input('Enter your password:  ')
password_length = len(password)

print('Hei, {username}! Your password {password} is {password_length} long '.format(username=username, password='*' * password_length, password_length=len(password)))