from connect.screen import clear_screen

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
