# File to contain 'Brain' class to contain all relevant info for current game
from connect.board import create_board
from connect.screen import clear_screen

class Brain:
    """
    Will store game information, what value for each tile of board.
    Print board with this information.
    Calculate if there is a successfull connect!
    """

    def __init__(self, player, rival, color):
        self.player = player
        self.rival = rival
        self.tiles = [["B","B","B","B","B","B","B"],
                      ["B","B","B","B","B","B","B"],
                      ["B","B","B","B","B","B","B"],
                      ["B","B","B","B","B","B","B"],
                      ["B","B","B","B","B","B","B"],
                      ["B","B","B","B","B","B","B"]]
        self.count = [0,0,0,0,0,0,0]
        self.available = [1,2,3,4,5,6,7]
        #self.color = color

    def print_board(self):
        clear_screen()
        create_board(self.tiles)

    def take_turn(self, choice, which):
        player_choice = choice
        color = which
        y = 5 - self.count[player_choice-1]
        self.tiles[y][player_choice-1] = self.color
        self.print_board()
        self.count[player_choice-1] = self.count[player_choice-1] + 1
        if self.count[player_choice-1] === 6:
            available.remove(player_choice)
        if which === "P":
            rival.rival_turn(self)
        elif which === "R":
            player.player_turn(self)

        