from user import User 
import random
import string

def main():
    greetings=['Hey', 'Hi', 'Wassup', 'Jambo']
    choice = ''
    while choice != '1' or choice != '2' or choice != '3':
        choice = input('Would you like to create an account or Login?'
                        '\n1. Create an account'
                        '\n2. Login to existing account'
                        '\n3. Exit'
                        '\n '
                        )

        if choice == '1': 
            """
                Account creation
            """
            def get_random_password(length=4): 
                char_set = string.ascii_letters
                return  str(random.randint(1000,9999)) + ''.join(random.choice(char_set)for _ in range(length))

            def confirm_account_creation():
                global repeat
                
                okay = input('Type OK to Confirm\n ')

                if okay == 'OK':
                    user = User(user_name, password)
                    User.save_user(user)
                    print('Account created, proceed to Login\n')
                    print(User.user_list)
                else:
                    print('Did not confirm, Type "OK" in uppercase\n')
                    repeat = True

            def create_user_account():
                global user_name
                global password
                global repeat
                global okay

                user_name = input('Enter your username\n ')
                pass_choice = input(' a. Generate password\n'
                                    ' b. Create Password\n ')
                
                if pass_choice == 'a':
                    password = get_random_password()
                    print(f'Your password is {password}') 
                    repeat = False
                    confirm_account_creation()
                    
                if pass_choice == 'b':
                    password = input('Enter your password\n ')
                    confirm_password = input('Confirm your password\n ')

                    if password != confirm_password:
                        print('Passwords did not match, Try again\n ')
                        repeat = True
                    else:
                        repeat = False
                        confirm_account_creation()

            create_user_account()
            while repeat == True:
                create_user_account()
                    
        if choice == '2':
            """
                Login section of the code
            """
            def confirm_user_exists():
                username = input('Enter your username')
                password = input('Enter your password')

                for user in User.user_list:
                    print(user.user_name)
                # while password != passcode or username != name:
                #     pass

            confirm_user_exists()
            
        if choice == '3':
            exit()

if __name__ == "__main__":
    main()

#  social = input('Enter the Socials Name,eg Instagram \n')
#         input(f' Enter your {social} username \n ')
#         input(f' Enter your {social} password \n ')
#         input(f' Confirm your {social} password \n ')