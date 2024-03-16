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
        self.tiles = [["B", "B", "B", "B", "B", "B", "B"],
                      ["B", "B", "B", "B", "B", "B", "B"],
                      ["B", "B", "B", "B", "B", "B", "B"],
                      ["B", "B", "B", "B", "B", "B", "B"],
                      ["B", "B", "B", "B", "B", "B", "B"],
                      ["B", "B", "B", "B", "B", "B", "B"]]
        self.count = [0, 0, 0, 0, 0, 0, 0]
        self.available = [1, 2, 3, 4, 5, 6, 7]
        self.message = ""

    # Calls function in board file with tiles list list.
    def print_board(self):
        clear_screen()
        create_board(self.tiles, self.available)

    # Recieves turn from either player or computer.
    # Will update all relevant variables and call gather_result.
    def take_turn(self, choice, which):
        player_choice = choice
        color = which
        y = 5 - self.count[player_choice-1]
        self.tiles[y][player_choice-1] = color
        self.print_board()
        self.count[player_choice-1] = self.count[player_choice-1] + 1
        if self.count[player_choice-1] == 6:
            self.available[player_choice-1] = "X"
        self.gather_result(color, player_choice-1, y)

    # Populate four specified lists based on choice from take_turn.
    # Will call check_results.
    def gather_result(self, which, x_pos, y_pos):
        # Everything with same x_pos
        vertical = []
        # Everything with same y_pos
        horizontal = []
        # With diagonals stop when x_pos reaches 0/6, when y_pos reaches 0/5
        # Increase/Decrease x_pos/y_pos the same
        diagonal_a = []
        # Increase/Decrease x_pos/y_pos flipped
        diagonal_b = []
        # Add values in same column as selected option
        for i in range(6):
            vertical.append(self.tiles[i][x_pos])
        # Add values in same row as selected option
        for j in range(7):
            horizontal.append(self.tiles[y_pos][j])
        # Add values in first diagonal of selected option
        finished_a = 0
        count = 0
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
        count = 1
        while finished_a == 1:
            if (x_pos + count > 6 or y_pos + count > 5):
                finished_a = 2
            else:
                if (x_pos + count) == 6:
                    diagonal_a.append(self.tiles[y_pos + count][x_pos + count])
                    finished_a = 2
                else:
                    if (y_pos + count) == 5:
                        diagonal_a.append(self.tiles
                                          [y_pos + count][x_pos + count])
                        finished_a = 2
                    else:
                        diagonal_a.append(self.tiles
                                          [y_pos + count][x_pos + count])
                        count = count + 1
        # Add values in second diagonal of selected option
        finished_b = 0
        count = 0
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
        count = 1
        while finished_b == 1:
            if (x_pos + count > 6 or y_pos - count < 0):
                finished_b = 2
            else:
                if (x_pos + count) == 6:
                    diagonal_b.append(self.tiles[y_pos - count][x_pos + count])
                    finished_b = 2
                else:
                    if (y_pos - count) == 0:
                        diagonal_b.append(self.tiles
                                          [y_pos - count][x_pos + count])
                        finished_b = 2
                    else:
                        diagonal_b.append(self.tiles
                                          [y_pos - count][x_pos + count])
                        count = count + 1
        self.check_result(which, x_pos, y_pos, vertical,
                          horizontal, diagonal_a, diagonal_b)

    # Will procede through each of the four arrays checking for a connection.
    # Call for win/loss based on out come.
    def check_result(self, which, x_pos, y_pos, vertical_list,
                     horizontal_list, diagonal_a_list, diagonal_b_list):
        done = False
        while done is False:
            highest = 0
            highest_pos = 0
            direction = "Vertical"
            # Check for vertical
            count = 0
            checked = False
            for a in range(6):
                if which == vertical_list[a]:
                    count = count + 1
                    if (count >= 4):
                        checked = True
                else:
                    if (checked is False):
                        if (count > highest):
                            highest = count
                            highest_pos = x_pos
                        count = 0
            if count >= 4:
                name = ""
                if (which == "P"):
                    name = "Player"
                elif (which == "R"):
                    name = "Computer"
                self.message = f"Vertical Connection by {name}!"
                print("                     " + self.message)
                self.player.end_game(self)
                done = True
            # Check for horizontal
            count = 0
            checked = False
            for b in range(7):
                if which == horizontal_list[b]:
                    count = count + 1
                    if (count >= 4):
                        checked = True
                else:
                    if (checked is False):
                        if (count > highest):
                            highest = count
                            highest_pos = x_pos
                            direction = "Horizontal"
                        count = 0
            if count >= 4:
                name = ""
                if (which == "P"):
                    name = "Player"
                elif (which == "R"):
                    name = "Computer"
                self.message = f"Horizontal Connection by {name}!"
                print("                     " + self.message)
                self.player.end_game(self)
                done = True
            # Check for diagonal_a
            if len(diagonal_a_list) >= 4:
                count = 0
                checked = False
                for c in range(len(diagonal_a_list)):
                    if which == diagonal_a_list[c]:
                        count = count + 1
                        if (count >= 4):
                            checked = True
                    else:
                        if (checked is False):
                            if (count > highest):
                                highest = count
                                highest_pos = x_pos
                                direction = "Horizontal"
                            count = 0
                if count >= 4:
                    name = ""
                    if (which == "P"):
                        name = "Player"
                    elif (which == "R"):
                        name = "Computer"
                    self.message = f"Diagonal Connection by {name}!"
                    print("                     " + self.message)
                    self.player.end_game(self)
                    done = True
            # Check for diagonal_b
            if len(diagonal_b_list) >= 4:
                count = 0
                checked = False
                for d in range(len(diagonal_b_list)):
                    if which == diagonal_b_list[d]:
                        count = count + 1
                        if (count >= 4):
                            checked = True
                    else:
                        if (checked is False):
                            if (count > highest):
                                highest = count
                                highest_pos = x_pos
                                direction = "Horizontal"
                            count = 0
                if count >= 4:
                    name = ""
                    if (which == "P"):
                        name = "Player"
                    elif (which == "R"):
                        name = "Computer"
                    self.message = f"Diagonal Connection by {name}!"
                    print("                     " + self.message)
                    self.player.end_game(self)
                    done = True

            if done is False:
                done = True
                if which == "P":
                    self.rival.rival_turn(self, highest_pos,
                                          direction, highest)
                elif which == "R":
                    self.player.player_turn(self)

    # Called by player class if issue with user input.
    # Will print board and win message again.
    def end_game(self, player):
        self.print_board()
        print(self.message)
