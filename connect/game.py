from connect.screen import clear_screen
from connect.brain import Brain
from connect.player import Player
from connect.rival import Rival

def start_game():
    clear_screen()
    player = Player("Test", "Red")
    rival = Rival("Bot", "Yellow")
    brain = Brain(player, rival)

    player.player_turn(brain)