from time import sleep

from rich.console import Console

from src.field_manager import FieldManager
from src.game_manager import GameManager
from src.table_renderer import TableRenderer

def main() -> None:
    console = Console()

    with console.status('Carregando...', spinner='aesthetic'):
        fm = FieldManager()
        tr = TableRenderer(console)
        gm = GameManager(fm, tr, console)
        
    console.clear()
    gm.start()

if __name__ == '__main__':
    main()