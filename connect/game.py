
from connect.brain import Brain
from connect.player import Player
from connect.rival import Rival
from connect.screen import clear_screen

def start_game():
    which_diff = (input("""
                    Please select a difficulty for the computer: \n
                                 1. Easy, 2. Hard \n"""))
    if (which_diff in ["1", "2"]):
        num = int(which_diff)
        if(num == 1):
            player = Player("Player", "Red")
            rival = Rival("Easy", "Yellow")
            brain = Brain(player, rival)
            brain.print_board()
            player.player_turn(brain)
        elif(num == 2):
            player = Player("Player", "Red")
            rival = Rival("Hard", "Yellow")
            brain = Brain(player, rival)
            brain.print_board()
            player.player_turn(brain)
    else:
        clear_screen()
        print("""
                            Please pick either 1 or 2 \n""")
        start_game()
        





    