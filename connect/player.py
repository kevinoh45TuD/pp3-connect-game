from connect.screen import clear_screen
from rich.text import Text
import sys

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
            while picked == False:
                choice = input("""
                Please pick an available option between 1-7 \n""")
                if len(choice) >= 2:
                    raise TypeError
                else:
                    if choice.isnumeric() == True:
                        num = int(choice)
                        if num in brain.available:
                            brain.take_turn(num, "P")
                            picked = True
                        else:
                            raise ValueError
                    elif choice.isalpha() == True:
                        if choice.lower() == "q":
                            sys.exit(0)
                        else:
                            raise TypeError
                    else:
                        raise TypeError
        except TypeError:
            print("""
            Please keep your input to 1 character!
            Your choice must be a number or Q to quit!""")
            self.player_turn(brain)
        except ValueError:
            print(f"""
            Please pick a column with available space! Available options {brain.available}""")
            self.player_turn(brain)
