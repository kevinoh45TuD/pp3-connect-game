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
        #With diagonals stop when x_pos reaches 0/6, when y_pos reaches 0/5
        #Increase/Decrease x_pos/y_pos the same
        diagonal_a = []
        #Increase/Decrease x_pos/y_pos flipped
        diagonal_b = []
        #Add values in same column as selected option
        for i in range(6):
            vertical.append(self.tiles[i][x_pos])
        print(vertical)
        #Add values in same row as selected option
        for j in range(7):
            horizontal.append(self.tiles[y_pos][j])
        print(horizontal)
        #Add values in first diagonal of selected option
        finished_a = 0
        count = 1
        temp = []
        while finished_a == 0:
            if (x_pos - count) == 0:
                temp.append(self.tiles[y_pos - count][x_pos - count])
                finished_a = 1
            else:
                if (y_pos - count) == 0:
                    temp.append(self.tiles[y_pos - count][x_pos - count])
                    finished_a = 1
                else:
                    temp.append(self.tiles[y_pos - count][x_pos - count])
                    count = count + 1
        count = 1
        for k in range(len(temp)):
            diagonal_a.append(temp[len(temp) - count])
            count = count + 1
        count = 0
        while finished_a == 1:
            if (x_pos + count) == 6:
                diagonal_a.append(self.tiles[y_pos + count][x_pos + count])
                finished_a = 2
            else:
                if (y_pos + count) == 5:
                    diagonal_a.append(self.tiles[y_pos + count][x_pos + count])
                    finished_a = 2
                else:
                    diagonal_a.append(self.tiles[y_pos + count][x_pos + count])
                    count = count + 1
        print(diagonal_a)
        #Add values in second diagonal of selected option
        finished_b = 0
        count = 1
        temp = []
        while finished_b == 0:
            if (x_pos - count) == 0:
                temp.append(self.tiles[y_pos + count][x_pos - count])
                finished_b = 1
            else:
                if (y_pos + count) == 5:
                    temp.append(self.tiles[y_pos + count][x_pos - count])
                    finished_b = 1
                else:
                    temp.append(self.tiles[y_pos + count][x_pos - count])
                    count = count + 1
        count = 1
        for k in range(len(temp)):
            diagonal_b.append(temp[len(temp) - count])
            count = count + 1
        count = 0
        while finished_b == 1:
            if (x_pos + count) == 6:
                diagonal_b.append(self.tiles[y_pos - count][x_pos + count])
                finished_b = 2
            else:
                if (y_pos - count) == 0:
                    diagonal_b.append(self.tiles[y_pos - count][x_pos + count])
                    finished_b = 2
                else:
                    diagonal_b.append(self.tiles[y_pos - count][x_pos + count])
                    count = count + 1
        print(diagonal_b)

        