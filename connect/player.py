from connect.screen import clear_screen

from rich.console import Console
import sys

class Player:
    """
    Will contain all necessary information for the player.
    Functions for taking turn and any other input from the user.
    """

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0
    
    def player_turn(self, brain):
        choice = 0
        picked = False

        try:
            while picked == False:
                console = Console()
                choice = console.input("""
                [bright_yellow]Please pick an available option between 1-7 (or 'Q' to quit)\n[bright_yellow]""")
                if len(choice) >= 2:
                    raise TypeError
                else:
                    if choice.isnumeric() == True:
                        num = int(choice)
                        if num in brain.available:
                            brain.take_turn(num, "P")
                            picked = True
                        else:
                            raise ValueError
                    elif choice.isalpha() == True:
                        if choice.lower() == "q":
                            #sys.exit(0)
                            from connect.start import start
                            start()
                        else:
                            raise TypeError
                    else:
                        raise TypeError
        except TypeError:
            brain.print_board()
            console = Console()
            console.print("""
            [bold bright_red]Please keep your input to 1 character!
            Your choice must be a number or Q to quit![bold bright_red]""")
            self.player_turn(brain)
        except ValueError:
            brain.print_board()
            console = Console()
            console.print(f"""
            [bold bright_red]Please pick a column with available space! Available options {brain.available}[bold bright_red]""")
            self.player_turn(brain)
