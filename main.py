from time import sleep

from rich.console import Console

from core.field_manager import FieldManager
from core.game_manager import GameManager
from ui.table_renderer import TableRenderer

def main() -> None:
    console = Console()

    with console.status('Carregando...', spinner='aesthetic'):
        fm = FieldManager()
        tr = TableRenderer(console)
        gm = GameManager(fm, tr, console)
        sleep(2)
        
    console.clear()
    gm.start()

if __name__ == '__main__':
    main()