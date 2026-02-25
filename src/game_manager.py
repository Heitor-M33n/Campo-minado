from __future__ import annotations
from typing import TYPE_CHECKING
from time import sleep, time

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import  Panel
from rich.text import Text
from rich import box

if TYPE_CHECKING:
    from table_renderer import TableRenderer
    from field_manager import FieldManager

class GameManager():
    def __init__(self, fm: FieldManager, tr: TableRenderer, console: Console):
        self.fm = fm
        self.tr = tr
        self.console = console

    def start(self):
        self.console.print('')
        self.console.rule(Text('Minesweeper 😆'), style='khaki1')
        sleep(1)
        self.mainloop()

    def mainloop(self):
        while True:
            self.console.print('', Panel('[white][blue]1.[/blue] Jogar 🎮\n[green]2.[/green] Tutorial 😴 [dim](Não implementado por enquanto)[/dim]\n[red]3.[/red] Recordes 🏆 [dim](Não implementado por enquanto)[/dim]\n[dark_blue]4.[/dark_blue] Sair 🚪[/white]', style='khaki1'))

            action = int(Prompt.ask('Insira a opção desejada', console=self.console, choices=('1', '2', '3', '4'), show_choices=False))

            match action:
                case 1:
                    self.gameloop()
                case 2:
                    self.tutorial()
                case 3:
                    pass
                case 4:
                    break

            self.console.clear()

    def gameloop(self):
        self.console.clear()
        self.console.print('', Panel('[white][blue]1.[/blue] Fácil [dim](5x5, 15% de densidade)[/dim]\n[green]2.[/green] Médio [dim](8x8, 20% de densidade)[/dim]\n[red]3.[/red] Difícil [dim](10x10, 25% de densidade)[/dim]\n[dark_blue]4.[/dark_blue] Insano [dim](15x15, 35% de densidade)[/dim]\n[dark_red]5.[/dark_red] Personalizado [dim](Não implementado por enquanto)[/dim]\n[cyan]6.[/cyan] Cancelar[/white]'))

        diff = int(Prompt.ask('Insira a dificuldade desejada', console=self.console, choices=('1', '2', '3', '4', '5', '6'), show_choices=False))

        if diff in range(1, 5):
            CHART = {1: 'fácil', 2: 'médio', 3: 'difícil', 4: 'insano'}
            self.fm.generate_basic_data(difficulty=CHART.get(diff, 'médio'))
        elif diff == 5:
            #fazer depois
            return
        else:
            return

        self.console.clear()
        self.tr.render_visible_field(self.fm.visible_render_data)
        mode = 'g'

        x = int(Prompt.ask('Insira a coordenada X', console=self.console, choices=([str(i) for i in range(1, self.fm.width + 1)]), show_choices=False))
        y = int(Prompt.ask('Insira a coordenada Y', console=self.console, choices=([str(i) for i in range(1, self.fm.width + 1)]), show_choices=False))

        self.fm.first_guess(x, y)

        while True:
            self.console.clear()
            self.tr.render_visible_field(self.fm.visible_render_data)

            mode = Prompt.ask('Insira "G" para revelar um quadrado, "F" para colocar uma bandeira', console=self.console, choices=('g', 'f'), default=mode, show_choices=False, show_default=False, case_sensitive=False)

            x = int(Prompt.ask('Insira a coordenada X (coluna)', console=self.console, choices=([str(i) for i in range(1, self.fm.width + 1)]), show_choices=False))
            y = int(Prompt.ask('Insira a coordenada Y (linha)', console=self.console, choices=([str(i) for i in range(1, self.fm.width + 1)]), show_choices=False))

            if mode.lower() == 'g':
                state = self.fm.reveal(x, y)
            else:
                state = self.fm.flag(x, y)

            if state == 'W':
                self.won()
                break
            elif state == 'L':
                self.lost()
                break

    def won(self):
        self.console.clear()
        self.tr._render_field(self.fm._render_data)
        self.console.print('Você venceu!', style='bold green')
        sleep(5)

    def lost(self):
        self.console.clear()
        self.tr.render_visible_field(self.fm.visible_render_data)
        self.console.print('Game over!', style='bold red')
        sleep(5)

    def tutorial(self):
        pass