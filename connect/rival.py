from connect.screen import clear_screen
import random

class Rival:
    """
    Will contain all necessary information for computer opponent.
    Take turn after player, two difficulty levels.
    Easy: Random select position based columns with space
    Hard: Specific selection based on preventing opponent from winning.
    """
    def __init__(self, difficulty, color):
        self.difficulty = difficulty
        self.color = color
        self.name = "Rival"
    #Called when it is computers turn. Determines moved based on difficulty. Passes move to brain's take turn function.
    def rival_turn(self, brain, x_pos, direction, highest):
        """"
        Use of random based on:
        https://www.w3schools.com/python/ref_random_choice.asp
        """
        if (self.difficulty == "Easy"):
            choice = random.choice(brain.available)
            brain.take_turn(choice, "R")
        elif (self.difficulty == "Hard"):
            if (highest > 2):
                if(direction == "Vertical"):
                    brain.take_turn(x_pos, "R")
                else:
                    if(x_pos <= 5):
                        brain.take_turn(x_pos+1, "R")
                    else:
                        brain.take_turn(x_pos-1, "R")
            else:
                choice = random.choice(brain.available)
                brain.take_turn(choice, "R")
