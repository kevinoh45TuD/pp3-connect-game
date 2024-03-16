from connect.game import start_game
from connect.brain import Brain
from connect.screen import clear_screen
from rich.console import Console
import sys

#Prints the game's title for the start screen
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
#Provides user with options for start menu. Validates user input and executes code based on choice.
def pick_option():
    """
    Original code from:
    https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/
    """
    which_option = (input("""
                    Please select an option: \n
                    1. Start Game \n
                    2. Game Info \n
                    3. Exit Application \n"""))
    if (which_option in ["1", "2", "3"]):
        num = int(which_option)
        if(num > 0 and num < 4):
            if(num == 1):
                clear_screen()
                start_game()
            elif(num == 2):
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
            elif(num == 3):
                sys.exit(0)
            else:
                clear_screen()
                print_title()
                print("There was an unknown issue.. \n")
                pick_option()
    else:
        clear_screen()
        print_title()
        print("Please pick an available option! 1, 2 or 3 are valid inputs! \n")
        pick_option()
#First function called when program starts. Calls for start menu's title and options to be printed.
def start():
    clear_screen()
    print_title()
    pick_option()
