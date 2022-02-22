from create_account import create_account
from login import login
from rich.console import Console
from rich import print

rich_colors = Console()

def run_main_app():
    choice = ''
    while choice != '1' or choice != '2' or choice != '3':
        rich_colors.rule("[bold red] MAIN DASHBOARD", style='bold magenta')
        choice = input('Would you like to create an account or Login?'
                        '\n1. Create an account'
                        '\n2. Login to existing account'
                        '\n3. Exit'
                        '\n'
                        ).strip()

        if choice == '1': 
            """
                Account creation
            """
            create_account()
                    
        elif choice == '2':
            """
                Login section of the code
            """
            login()

        elif choice == '3':
            '''
                Exit out of application
            '''
            exit()
        else:
            print('[bold red]Choice not available, Pick between [bold green]1, 2[/bold green] and [bold green]3.')

if __name__ == "__main__":
    run_main_app()