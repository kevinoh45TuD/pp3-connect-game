from rich.console import Console
from rich.table import Table
from rich import box
from rich.align import Align

def print_board():
    console = Console()
    
    tile = """###\n###\n###"""

    table = Table(title="Connect 4", box=box.DOUBLE, style="blue3", show_lines=True)

    table.add_column(tile, style="bright_black", no_wrap=True, justify="center", width=5)
    table.add_column(tile, style="bright_black", justify="center", width=5)
    table.add_column(tile, style="bright_black", justify="center", width=5)
    table.add_column(tile, style="bright_black", justify="center", width=5)
    table.add_column(tile, style="bright_black", justify="center", width=5)
    table.add_column(tile, style="bright_black", justify="center", width=5)
    table.add_column(tile, style="bright_black", justify="center", width=5)

    table.add_row(tile, tile, tile, tile, tile, tile, tile)
    table.add_row(tile, tile, tile, tile, tile, tile, tile)
    table.add_row(tile, tile, tile, tile, tile, tile, tile)
    table.add_row(tile, tile, tile, tile, tile, tile, tile)
    table.add_row(tile, tile, tile, tile, tile, tile, tile)

    table = Align.center(table, vertical="middle")

    console.print(table)