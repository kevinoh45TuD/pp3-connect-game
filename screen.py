import os

def clear_screen():
    """
    Clear the terminal screen when needed.
    """
    os.system('cls' if os.name == 'nt' else 'clear')