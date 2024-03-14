from connect.game import start_game
from connect.brain import Brain
from connect.screen import clear_screen
from rich.console import Console
import sys

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

def pick_option():
    which_option = int(input("""
    Please select an option: \n
    1. Start Game \n
    2. Game Info \n
    3. Exit Application \n"""))
    if(which_option > 0 and which_option < 4):
        if(which_option == 1):
            start_game()
        elif(which_option == 2):
            clear_screen()
            print("""
                                           Connect 4 \n
            The goal of the game is to use your tokens to create a row of \n
            at least 4 tokens. \n
            This row can be vertical, horizontal or diagonal. \n
            You will take turns with the computer to select a column \n
            to drop your token. \n
            Player color will be 'Red' while computer color will be 'Yellow' \n""")
            pick_option()
        elif(which_option == 3):
            sys.exit(0)
    else:
        start()
        print("Please pick an available option! \n")

def start():
    clear_screen()
    print_title()
    pick_option()
