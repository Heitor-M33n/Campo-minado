from time import sleep

from rich.console import Console

from core.field_manager import FieldManager
from core.game_manager import GameManager
from ui.table_renderer import TableRenderer
from ui.input_handler import InputHandler
from ui.ui_handler import UiHandler

def main() -> None:
    console = Console()

    with console.status('Carregando...', spinner='aesthetic'):
        fm = FieldManager()
        tr = TableRenderer(console)
        ih = InputHandler(console)
        uh = UiHandler(console)
        gm = GameManager(fm, tr, ih, uh)
        sleep(2)
        
    console.clear()
    gm.start()

if __name__ == '__main__':
    main()