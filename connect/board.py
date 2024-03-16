from rich.console import Console
from rich.table import Table
from rich import box
from rich.align import Align

def create_board(array, available):
    """
    Unpacking list help from:
    https://stackoverflow.com/questions/65216850/list-of-lists-into-a-python-rich-table
    """
    console = Console()
    
    tile = """##\n##"""

    table = Table(title="Connect 4", box=box.DOUBLE, style="blue3", show_lines=True, header_style="white")

    table.add_column(str(available[0]), style="bright_black", no_wrap=True, justify="center", width=5)
    table.add_column(str(available[1]), style="bright_black", justify="center", width=5)
    table.add_column(str(available[2]), style="bright_black", justify="center", width=5)
    table.add_column(str(available[3]), style="bright_black", justify="center", width=5)
    table.add_column(str(available[4]), style="bright_black", justify="center", width=5)
    table.add_column(str(available[5]), style="bright_black", justify="center", width=5)
    table.add_column(str(available[6]), style="bright_black", justify="center", width=5)

    for y in range(6):
        tiles = []
        for x in range(7):
            if array[y][x] == "B":
                tile = """#"""
                tiles.append(tile)
            elif array[y][x] == "P":
                tile = """[bold bright_red]#[bold bright_red]"""
                tiles.append(tile)
            elif array[y][x] == "R":
                tile = """[bold bright_yellow]#[bold bright_yellow]"""
                tiles.append(tile)
        table.add_row(*tiles) 

    table = Align.center(table, vertical="middle")

    console.print(table)