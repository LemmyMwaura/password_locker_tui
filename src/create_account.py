from models.user import User 
from rich import print
import random
import string

def create_account():
    def get_random_password(length=4): 
        char_set = string.ascii_letters
        return  str(random.randint(1000,9999)) + ''.join(random.choice(char_set)for _ in range(length))

    def confirm_account_creation():
        global wrong_password
        
        okay = input('Type OK to Confirm\n').strip()

        if okay == 'OK':
            user = User(user_name, password)
            User.save_user(user)
            print('[bold green]Account created, proceed to Login\n')
        else:
            print('[bold red]Did not confirm, Type [bold green]"OK"[/bold green] in uppercase\n')
            wrong_password = True

    def confirm_username_exists(username):
        for user in User.user_list:
            if username == user.user_name:
                print('Username taken, Try login in or pick a different username')
                return False
            break
        return True

    def create_user_account():
        global user_name
        global password
        global wrong_password
        global okay

        user_name = input('Enter your username\n').strip()
        if confirm_username_exists(user_name) == True:
            print('[bold blue]Generate or Create Password')
            pass_choice = input(' a. Generate password\n'
                                ' b. Create Password\n'
                                ).strip()

            if pass_choice == 'a':
                password = get_random_password()
                print(f'[bold green]Your password is [bold blue]{password}') 
                wrong_password = False
                confirm_account_creation()
                
            elif pass_choice == 'b':
                password = input('Enter your password\n').strip()
                confirm_password = input('Confirm your password\n').strip()

                if password != confirm_password:
                    print('[bold red]Passwords did not match, Try again\n')
                    wrong_password = True
                else:
                    wrong_password = False
                    confirm_account_creation()

            else:
                print('[bold red]Option not available, pick between [bold green]a[/bold green] and [bold green]b')
                wrong_password = True

    create_user_account()

    while wrong_password == True:
        create_user_account()