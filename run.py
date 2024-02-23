# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def get_user_name():
    """Ask user's name to begin"""
    user_name = input("What is your name? \n")
    print(f"Welcome {user_name}!")

get_user_name()