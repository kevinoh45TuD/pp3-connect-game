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
    brain = Brain("Player", "Rival", "Y")
    brain.take_turn()
