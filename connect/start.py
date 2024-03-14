from connect.game import start_game
from connect.brain import Brain

def print_title():
    print("""
         ###  ####  #####  #####  ####   ###  #####    
        #     #  #  #   #  #   #  #     #       #
        #     #  #  #   #  #   #  ####  #       #
        #     #  #  #   #  #   #  #     #       #
         ###  ####  #   #  #   #  ####   ###    #\n""")

def get_user_name():
    """Ask user's name to begin"""
    user_name = input("What is your name? \n")
    if user_name.isalpha():
        print(f"Welcome {user_name}!")
    else:
        print("You must only enter letters please")
        get_user_name()

def start():
    start_game()
    #brain = Brain("player", "rival")
    #brain.gather_result("P", 3, 2)
