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
    
    def player_turn(self, brain):
        choice = 0
        picked = False

        try:
            while picked === False:
                choice = int(input("""
                Please pick and available option between 1-7"""))
                if choice in brain.available:
                    brain.take_turn(choice)
                    picked = True
                else:
                    raise ValueError
        except TypeError:
            print("""
            Your choice must be a number!""")
            clear_screen()
            self.player_turn(brain)
        except ValueError:
            print("""
            Please pick a column with available space!""")
            clear_screen()
            self.player_turn(brain)
