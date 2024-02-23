# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def get_user_name():
    """Ask user's name to begin"""
    user_name = input("What is your name? \n")
    if user_name.isalpha():
        print(f"Welcome {user_name}!")
    else:
        print("You must only enter letters please")
        get_user_name()

get_user_name()