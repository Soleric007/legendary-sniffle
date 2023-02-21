name = input('Hello User, What is your name: ')
realpasword = 'solomon'
password = input('Hello ' + name + ' Welcome, please input your Password: ')
if len(password) > 9:
    print('Password Exceeds the specific Number needed')
elif password == realpasword:
    print('Access Granted, Welcome ' + name)
else:
    print('Access Denied')


