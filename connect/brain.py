# File to contain 'Brain' class to contain all relevant info for current game
from connect.board import print_board

class Brain:
    """
    Will store game information, what value for each tile of board.
    Print board with this information.
    Calculate if there is a successfull connect!
    """

    def __init__(self, player, rival):
        self.player = player
        self.rival = rival
        self.tiles = [["B","B","B","B","B","B","B"],
                      ["B","B","B","B","B","B","B"],
                      ["B","B","B","B","B","B","B"],
                      ["B","B","B","Y","B","B","B"],
                      ["B","B","B","Y","B","B","B"],
                      ["B","R","R","Y","B","B","B"]]
        self.count = [0,0,0,0,0,0,0]