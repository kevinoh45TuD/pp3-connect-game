from connect.screen import clear_screen

class Player:
    """
    Will contain all necessary information for the player.
    Functions for taking turn and any other input from the user.
    """

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0
    
    
