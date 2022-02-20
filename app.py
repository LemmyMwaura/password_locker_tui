from user import User 
from credentials import Credential
from rich.table import Table
from rich.console import Console
import random
import string

rich_colors = Console()
def run_main_app():
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
            def check_if_user_exists():
                pass

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
                else:
                    print('Did not confirm, Type "OK" in uppercase\n')
                    repeat = True

            def create_user_account():
                global user_name
                global password
                global repeat
                global okay

                user_name = input('Enter your username\n ')

                #TODO check if user exists
                check_if_user_exists()
                print('Generate or Create Password')
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
            def add_credential():
                if social_password != social_confirm_password:
                    print('Passwords don\'t match try again') 
                else:
                    new_credential = Credential(social, social_username, social_password)
                    current_user.credential_list.append(new_credential)
                    print(current_user.credential_list)
                    print(f'Your {social} password has been saved')

            def append_to_table():
                    table = Table(title = f"{current_user.user_name}'s Credentials")
                    table.add_column('Social-Account', style='bold cyan')
                    table.add_column('Social-Username', style='bold magenta')
                    table.add_column('Password', justify='right', style='bold green')

                    for credential in current_user.credential_list:
                        table.add_row(credential.social_account_name,
                                    credential.social_username,
                                    credential.social_password,
                                )
                    rich_colors.print(table)

            def access_personal_details():
                global social
                global social_username
                global social_password
                global social_confirm_password

                pick = input('Would you like to save a new password or view existing passwords\n'
                                'a. Save a new password\n'
                                'b. View my current password(s)\n '
                            )
                if pick == 'a':
                    social = input('Enter the Social Account Name,eg Instagram \n')
                    social_username = input(f'Enter your {social} username \n ')
                    social_password = input(f'Enter your {social} password \n ')
                    social_confirm_password = input(f'Confirm your {social} password \n ')

                    add_credential()
                if pick == 'b':
                    append_to_table()
                
            def confirm_user_exists():
                global current_user

                username = input('Enter your username\n ')
                password = input('Enter your password\n ')

                for idx, user in enumerate(User.user_list): 
                    if username in user.user_name:
                        print(f'Jambo {username}\n')
                        current_user = User.user_list[idx]

                        if password != user.password:
                            print(f'Your password was wrong {user.user_name}, try again')
                        else:   
                            access_personal_details()  
                    else:
                        print('Username not available, Create account or try again.')

            confirm_user_exists()

        if choice == '3':
            exit()

if __name__ == "__main__":
    run_main_app()

