# File to contain 'Brain' class to contain all relevant info for current game
from connect.board import create_board
from connect.screen import clear_screen

class Brain:
    """
    Will store game information, what value for each tile of board.
    Print board with this information.
    Calculate if there is a successfull connect!
    """

    def __init__(self, player, rival):
        self.player = player
        self.rival = rival
        self.tiles = [["B","A","B","7","B","F","B"],
                      ["B","B","B","8","G","B","B"],
                      ["1","2","3","P","4","5","6"],
                      ["B","B","H","9","C","B","B"],
                      ["B","I","B","10","B","D","B"],
                      ["J","B","B","11","B","B","E"]]
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
        self.tiles[y][player_choice-1] = color
        self.print_board()
        self.count[player_choice-1] = self.count[player_choice-1] + 1
        if self.count[player_choice-1] == 6:
            self.available.remove(player_choice)
        if which == "P":
            self.rival.rival_turn(self)
        elif which == "R":
            self.player.player_turn(self)

    def gather_result(self, which, x_pos, y_pos):
        #Everything with same x_pos
        vertical = []
        #Everything with same y_pos
        horizontal = []
        #Increase/Decrease x_pos/y_pos the same
        diagonal_a = []
        #Increase/Decrease x_pos/y_pos flipped
        diagonal_b = []
        #With diagonals stop when x_pos reaches 0/6, when y_pos reaches 0/5
        for i in range(6):
            vertical.append(self.tiles[i][x_pos])
        print(vertical)


        