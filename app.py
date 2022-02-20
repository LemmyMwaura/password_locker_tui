from user import User 

choice = ''
while choice != '1' or choice != '2' or choice != '3':
    choice = input('Would you like to create an account or Login?'
                    '\n1. Create an account'
                    '\n2. Login to existing account'
                    '\n3. Exit'
                    '\n'
                    )

    if choice == '1': 
        def create_account():
            global user_name
            global password
            global confirm_password
            global repeat

            user_name = input('Enter your username\n ')
            password = input('Enter your password\n ')
            confirm_password = input('Confirm your password\n ')

            if password != confirm_password:
                print('Passwords did not match, Try again\n')
                repeat = True
            else:
                okay = input('Type OK to Confirm\n ')

        if repeat == True:
            create_account()
            
        create_account()
            
    if choice == '2':
        print('welcome')
    if choice == '3':
        exit()


#  social = input('Enter the Socials Name,eg Instagram \n')
#         input(f' Enter your {social} username \n ')
#         input(f' Enter your {social} password \n ')
#         input(f' Confirm your {social} password \n ')