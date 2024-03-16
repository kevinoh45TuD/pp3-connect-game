from connect.screen import clear_screen
from rich.console import Console

class Player:
    """
    Will contain all necessary information for the player.
    Functions for taking turn and any other input from the user.
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0
    #Called initial after board load, also called after computer turn. Validates input and passes to brain.
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
                [bold bright_red]Please pick a column with available space!\n                 Available options {brain.available}[bold bright_red]""")
            self.player_turn(brain)
    #Called when game is won by either player. Will validate input and start new game or return to start menu.
    def end_game(self, brain):
        try:
            console = Console()
            which_option = console.input("""
                [bright_yellow]Would you like to: 1. Restart, 2. Quit \n[bright_yellow]""")
            if (len(which_option) >= 2):
                raise TypeError
            else:
                if (which_option.isnumeric() == True):
                    num = int(which_option)
                    if (num == 1 or num == 2):
                        if (num == 1):
                            from connect.game import start_game
                            start_game()
                        elif (num == 2):
                            from connect.start import start
                            start()
                    else:
                        raise ValueError
                else:
                    raise TypeError
        except TypeError:
            brain.end_game(self)
            console = Console()
            console.print("[bold bright_red]Input must be one character and a number![bold bright_red]")
            self.end_game(brain)
        except ValueError:
            brain.end_game(self)
            console = Console()
            console.print("[bold bright_red]Please pick 1 or 2![bold bright_red]")
            self.end_game(brain)
