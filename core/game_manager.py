from __future__ import annotations
from typing import TYPE_CHECKING

from rich.console import Console
from rich.prompt import Prompt

if TYPE_CHECKING:
    from ..ui.table_renderer import TableRenderer
    from field_manager import FieldManager

class GameManager():
    def __init__(self, fm: FieldManager, tr: TableRenderer, console: Console):
        self.fm = fm
        self.tr = tr
        self.console = console

    def start(self):
        self.console.rule('Minesweeper')
        self.console.print('')
        self.mainloop()

    def mainloop(self):
        while True:
            self.console.print('1. Jogar')

            action = int(Prompt.ask('Insira a opção desejada', console=self.console, choices=('1', '2', '3'), show_choices=False))

            match action:
                case 1:
                    self.gameloop()
                case 2:
                    pass
                case 3:
                    pass
                case _:
                    pass

    def gameloop(self):
        self.console.print('1. Fácil (5x5, 15% de densidade)')
        self.console.print('2. Médio (8x8, 20% de densidade)')
        self.console.print('3. Difícil (10x10, 25% de densidade)')
        self.console.print('4. Insano (15x15, 35% de densidade)')
        self.console.print('5. Personalizado')

        diff = int(Prompt.ask('Insira a dificuldade desejada', console=self.console, choices=('1', '2', '3', '4', '5'), show_choices=False))

        if diff != 5:
            CHART = {1: 'fácil', 2: 'médio', 3: 'difícil', 4: 'insano'}
            self.fm.generate_basic_data(difficulty=CHART.get(diff, 'médio'))
        else:
            #fazer depois
            self.fm.generate_basic_data(difficulty=CHART.get('médio'))

        mode = 'guess'
        self.tr.render_visible_field(self.fm.render_data)

        x = int(Prompt.ask('Insira a coordenada X', console=self.console, choices=([str(i) for i in range(1, self.fm.width + 1)]), show_choices=False))
        y = int(Prompt.ask('Insira a coordenada Y', console=self.console, choices=([str(i) for i in range(1, self.fm.width + 1)]), show_choices=False))

        self.fm.first_guess(x, y)

        while True:
            self.tr.render_visible_field(self.fm.render_data)

            mode = Prompt.ask('Insira "G" para revelar um quadrado, "F" para colocar uma bandeira', console=self.console, choices=('g', 'f'), default=mode, show_choices=False, show_default=False, case_sensitive=False)

            x = int(Prompt.ask('Insira a coordenada X', console=self.console, choices=([str(i) for i in range(1, self.fm.width + 1)]), show_choices=False))
            y = int(Prompt.ask('Insira a coordenada Y', console=self.console, choices=([str(i) for i in range(1, self.fm.width + 1)]), show_choices=False))

            if mode.lower() == 'g':
                self.fm.reveal(x, y)
            else:
                self.fm.flag(x, y)

    def win(self):
        pass

    def lose(self):
        pass

    def tutorial(self):
        pass