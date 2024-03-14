
from connect.brain import Brain
from connect.player import Player
from connect.rival import Rival

def start_game():
    
    player = Player("Test", "Red")
    rival = Rival("Hard", "Yellow")
    brain = Brain(player, rival)
    brain.print_board()
    player.player_turn(brain)