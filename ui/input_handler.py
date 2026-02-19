from rich.console import Console
from rich.prompt import Prompt

class InputHandler():
    def __init__(self, console: Console) -> None:
        self.console = console

    def prompt_chords(self, width: int) -> tuple:
        #para fazer
        x = Prompt.ask('Insira a coordenada X', console=self.console, choices=([str(i) for i in range(1, width + 1)]), show_choices=False)
        y = Prompt.ask('Insira a coordenada Y', console=self.console, choices=([str(i) for i in range(1, width + 1)]), show_choices=False)
        return (int(x), int(y))

    def prompt_options(self) -> int:
        #para fazer
        return int(Prompt.ask('Insira a opção desejada', console=self.console, choices=('1'), show_choices=False))

    def prompt_difficulty(self) -> int:
        #para fazer
        return int(Prompt.ask('Insira a dificuldade desejada', console=self.console, choices=('1', '2', '3', '4', '5'), show_choices=False))
    
    def personal_difficulty(self) -> tuple:
        pass