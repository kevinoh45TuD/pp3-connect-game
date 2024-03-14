from connect.game import start_game
from connect.brain import Brain
from rich.console import Console

def print_title():
    console = Console()
    title_connect = ("""[bright_yellow]
         ###  ####  #####  #####  ####   ###  #####            
        #     #  #  #   #  #   #  #     #       #               
        #     #  #  #   #  #   #  ####  #       #                
        #     #  #  #   #  #   #  #     #       #                
         ###  ####  #   #  #   #  ####   ###    #[bright_yellow]""")
            
    title_four = ("""[bright_red]
                         #    #
                         #    #
                         ######
                              #
                              #[bright_red]\n""")
    console.print(title_connect, title_four)

def get_user_name():
    """Ask user's name to begin"""
    user_name = input("What is your name? \n")
    if user_name.isalpha():
        print(f"Welcome {user_name}!")
    else:
        print("You must only enter letters please")
        get_user_name()

def start():
    print_title()
    
