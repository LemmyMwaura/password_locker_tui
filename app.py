from user import User 

choice = ''
while choice != '1' or choice != '2' or choice != '3':
    choice = input('Would you like to create an account or Login?'
                    '\n 1. Create an account'
                    '\n 2. Login to existing account'
                    '\n 3. Exit'
                    '\n '
                    )

    if choice == '1':
        print('good choice')
    if choice == '2':
        print('welcome')
    if choice == '3':
        exit()
