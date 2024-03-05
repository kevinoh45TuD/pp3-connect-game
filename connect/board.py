from rich.console import Console
from rich.table import Table
from rich import box
from rich.align import Align

def print_board():
    console = Console()
    
    tile = """##\n##"""

    table = Table(title="Connect 4", box=box.DOUBLE, style="blue3", show_lines=True, header_style="white")

    table.add_column("1", style="bright_black", no_wrap=True, justify="center", width=5)
    table.add_column("2", style="bright_black", justify="center", width=5)
    table.add_column("3", style="bright_black", justify="center", width=5)
    table.add_column("4", style="bright_black", justify="center", width=5)
    table.add_column("5", style="bright_black", justify="center", width=5)
    table.add_column("6", style="bright_black", justify="center", width=5)
    table.add_column("7", style="bright_black", justify="center", width=5)

    table.add_row(tile, tile, tile, tile, tile, tile, tile)
    table.add_row(tile, tile, tile, tile, tile, tile, tile)
    table.add_row(tile, tile, tile, tile, tile, tile, tile)
    table.add_row(tile, tile, tile, tile, tile, tile, tile)
    table.add_row(tile, tile, tile, tile, tile, tile, tile)
    table.add_row(tile, tile, tile, tile, tile, tile, tile)

    table = Align.center(table, vertical="middle")

    console.print(table)