from user import User 
from credentials import Credential
from rich.console import Console
from rich.table import Table
from rich import print
import random
import string

rich_colors = Console()

def login():
    def get_random_password(length=4): 
        char_set = string.ascii_letters
        return  str(random.randint(1000,9999)) + ''.join(random.choice(char_set)for _ in range(length))

    def add_credential(social, social_username, social_password):
        new_credential = Credential(social, social_username, social_password)
        current_user.credential_list.append(new_credential)
        print(f'[bold green]Your [bold blue]{social}[/bold blue] password has been saved')

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

    def delete_password():
        append_to_table()
        delete_item = input('Enter Social-Account name you wish to delete\n').strip()

        for credential in current_user.credential_list:
            if delete_item == credential.social_account_name:
                remove = input(f'Are you sure you want to delete {delete_item}\n'
                        'Type "Yes" if sure\n'
                    ).strip()
                if remove == 'Yes':
                    current_user.credential_list.remove(credential)   
                    print(f'[bold blue]{delete_item} [bold green]was successfully removed')
                else:   
                    print(f'[bold red]Did not type "Yes", [bold blue]{delete_item}[/bold blue] credential was not removed')
                break
        else:
            print('[bold red]Account does not exit, try again')

    def access_personal_details():
        logged_in = True

        while logged_in:
            rich_colors.rule("[bold red] LOGIN DASHBOARD", style='bold magenta')
            pick = input('Would you like to save a new password or view existing passwords\n'
                            '1. Save a new password\n'
                            '2. View my current password(s)\n'
                            '3. Delete password(s)\n'
                            '4. LogOut\n'
                        ).strip()
            if pick == '1':
                social = input('Enter the Social Account Name,eg Instagram \n').strip()
                social_username = input(f'Enter your {social} username \n').strip()
                print('[bold blue]Generate or Create your social Password')
                pass_choice = input(' a. Generate password\n'
                                    ' b. Create Password\n'
                                    ).strip()

                if  pass_choice == 'a':
                    social_password = get_random_password()
                    print(f'[bold green]Your password is [bold blue]{social_password}')
                    confirm = input('Type OK to confirm\n').strip()
                    if confirm == 'OK':
                        add_credential(social, social_username, social_password)
                    else:
                        print(f'[bold red]Did not confirm, [bold blue]{social}[/bold blue] Account not created')

                elif pass_choice == 'b':
                    social_password = input('Enter your password\n').strip()
                    social_confirm_password = input('Confirm your password\n').strip()

                    if social_password != social_confirm_password:
                        print('[bold red]Passwords don\'t match try again') 
                    else:
                        add_credential(social, social_username, social_password)

            elif pick == '2':
                append_to_table()

            elif pick == '3':
                delete_password()

            elif pick == '4':
                logged_in = False

            else:
                print('[bold red]Option not available, Try again')

    def confirm_user_exists():
        global current_user

        username = input('Enter your username\n').strip()
        password = input('Enter your password\n').strip()

        for idx, user in enumerate(User.user_list): 
            if username == user.user_name:
                print(f'[bold blue]Jambo {username}\n')
                current_user = User.user_list[idx]

                if password != user.password:
                    print(f'[bold red]Your password was wrong [bold blue]{username}[/bold blue], try again')
                else:   
                    access_personal_details()  
                break
        else:
            print('[bold red]Username not available, Create account or try again.')      

    confirm_user_exists()