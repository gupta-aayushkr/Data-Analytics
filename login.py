uname = 'Admin'
pwd = 'admin123'


while True:
    attempt += 1
    print(f'Attempt {attempt} of 5')
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    if attempt == 3:
        print('Too many attempts')
        break
    if username != uname:
        print("Invalid Username")
    if password != pwd:
        print("Invalid Password")
    if username == uname and password == pwd:
        print('Login Successful')
        break