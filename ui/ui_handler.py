from rich.console import Console
from rich.style import Style
from rich.text import Text

#Text('', Style(''))
#para copiar e colar

class UiHandler():
    def __init__(self, console: Console) -> None:
        self.console = console

    def intro(self):
        #para fazer
        self.console.rule('Minesweeper')
        self.console.print('')

    def display_options(self):
        #para fazer
        self.console.print('1. Jogar')

    def display_difficulty(self):
        self.console.print('1. Fácil (5x5, 15% de densidade)')
        self.console.print('2. Médio (8x8, 20% de densidade)')
        self.console.print('3. Difícil (10x10, 25% de densidade)')
        self.console.print('4. Insano (15x15, 35% de densidade)')
        self.console.print('5. Personalizado')
