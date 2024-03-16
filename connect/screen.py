import os

#Standalone function used frequently to clear the screen.
def clear_screen():
    """
    Clear the terminal screen when needed.
    Original code from:
    https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')