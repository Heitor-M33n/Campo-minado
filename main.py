from time import sleep

from rich.console import Console

from models.table_renderer import Table_renderer
from models.field_manager import Field_manager
from models.game_manager import Game_manager

console = Console()

with console.status('Carregando...', spinner='aesthetic'):
    fm = Field_manager()
    tr = Table_renderer()
    gm = Game_manager(console, fm, tr)
    
console.clear()
console.rule('teste')
fm.generate_basic_data(difficulty='difícil')
fm.first_guess(5, 5)
console.print(tr.render_visible_field(fm.render_data))