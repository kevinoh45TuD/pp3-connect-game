from rich.console import Console
from rich.table import Table
from rich import box

def print_board():
    console = Console()
    
    table = Table(title="Connect 4", box=box.DOUBLE, style="blue3")
    table.add_column("#", style="grey", no_wrap=true)
    table.add_column("#", style="grey")
    table.add_column("#", style="grey")
    table.add_row("#", "#", "#")
    table.add_row("#", "#", "#")