import time
from start import print_title
from screen import clear_screen

def get_user_name():
    """Ask user's name to begin"""
    user_name = input("What is your name? \n")
    if user_name.isalpha():
        print(f"Welcome {user_name}!")
    else:
        print("You must only enter letters please")
        get_user_name()

print_title()
time.sleep(3)
clear_screen()
get_user_name()

#pip3 freeze > requirements.txt