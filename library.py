from random import randrange
from time import sleep

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text
from rich import box

console = Console()

class FieldManager:
    def __init__(self) -> None:
        self.clear()

    def __repr__(self) -> str:
        return f'difficulty: {self.__difficulty}\nwidth: {self.__width}\nsize: {self.__size}\ndensity: {self.__density}\nbombs: {self.__bombs}\nbomb_chords: {self.__bomb_chords}\nfield:\n{self.__field}\nplay_field:\n{self.play_field}'
    
    def play(self) -> None:
        playing = True

        while playing:
            console.clear()
            console.print(self.play_field_rich)

            if self.__field == self.__play_field:
                self.win()

            x = int(Prompt.ask('Insira a coordenada X', choices=list(str(item) for item in range(1, self.__width + 1)), show_choices=False))
            y = int(Prompt.ask('Insira a coordenada Y', choices=list(str(item) for item in range(1, self.__width + 1)), show_choices=False))

            playing = self.guess(x, y)

        console.clear()
        console.print(self.play_field_rich)
        self.game_over()

    def guess(self, x: int, y: int) -> bool:
        #coordenadas visuais, n reais
        real_y = self.__width - y
        real_x = x - 1
        tile = self.__field[real_y][real_x]

        if tile == 'X':
            self.__play_field[real_y][real_x] = self.__field[real_y][real_x]
            return False
        elif tile != ' ':
            self.__play_field[real_y][real_x] = self.__field[real_y][real_x]
            return True
        
        self.__play_field[real_y][real_x] = self.__field[real_y][real_x]
        return True

    def game_over(self) -> None:
        #fazer uma animação top, do campo revelando em cascata
        console.print('\nGame over\n')

    def win(self) -> None:
        console.print('\nVocê venceu!\n')

    def clear(self) -> None:
        self.__difficulty = ''
        self.__width = 0
        self.__size = 0
        self.__density = 0
        self.__bombs = 0
        self.__bomb_chords = []
        self.__field = []
        self.__play_field = []

    def generate(self, width: int = 0, density_percentage: int = 0, difficulty: str = ''):
        DIFF_CHART = {'fácil': (5, 15), 'médio': (8, 20), 'difícil': (10, 25), 'insano': (15, 35)} 
        self.clear()

        if not difficulty:
            self.__width = width
            self.__density = density_percentage / 100
            self.__difficulty = 'personalizado'
        else:
            self.__width = DIFF_CHART[difficulty][0]
            self.__density = DIFF_CHART[difficulty][1] / 100
            self.__difficulty = difficulty

        self.__size = self.__width * self.__width
        self.__bombs = int(round(self.__density * self.__size))

        #gerar coordenadas
        for _ in range(self.__bombs):
            while True:
                x, y = randrange(self.__width), randrange(self.__width)
                x += 1
                y += 1
                if f'{x}, {y}' not in self.__bomb_chords:
                    self.__bomb_chords.append(f'{x}, {y}')
                    break

        #gerar matriz
        for y in range(self.__width):
            self.__field.append([])
            for _ in range(self.__width):
                self.__field[y].append('')

        #posicionar bombas
        #são posicionadas usando coordenadas do plano cartesiano, lógica um pouco confusa
        for visual_x in range(1, self.__width + 1):
            visual_y = 1
            real_y = self.__width - 1
            while visual_y < self.__width + 1:
                if f'{visual_x}, {visual_y}' in self.__bomb_chords:
                    self.__field[real_y][visual_x - 1] = 'X'

                real_y -= 1
                visual_y += 1

        #gerar demais tiles
        for y in range(self.__width):
            for x in range(self.__width):
                if self.__field[y][x] == 'X':
                    continue
                
                #descobrir número do tile
                bombs = 0
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if 0 <= y + a < self.__width and 0 <= x + b < self.__width and self.__field[y + a][x + b] == 'X':
                            bombs += 1


                if bombs == 0:
                    bombs = ' '

                self.__field[y][x] = str(bombs)

        #gerar matriz com tiles escondidos
        for y in range(self.__width):
            self.__play_field.append([])
            for _ in range(self.__width):
                self.__play_field[y].append('?')

    @property
    def width(self) -> int:
        return self.__width
    
    @property
    def size(self) -> int:
        return self.__size

    @property
    def density(self) -> float:
        return self.__density
    
    @property
    def bombs(self) -> int:
        return self.__bombs

    @property
    def difficulty(self) -> str:
        return self.__difficulty

    @property
    def play_field(self) -> list:
        return self.__play_field
    
    @property
    def play_field_rich(self) -> Table:
        COLORS = {'?': 'grey_70', 'X': 'bright_red', ' ': 'white', '1': 'blue', '2': 'green', '3': 'red', '4': 'dark_blue', '5': 'dark_red', '6': 'cyan', '7': 'grey_60', '8': 'grey_50'}

        table = Table(title=self.__difficulty, box=box.HEAVY_EDGE, show_header=False, show_lines=True)

        for i in range(self.__width):
            y = Text(str(self.__width - i), '')
            row = list(Text(str(item), f'{COLORS[item]}') for item in self.__play_field[i])

            table.add_row(y, *row)

        x = list(Text(str(item)) for item in range(self.__width + 1))
        table.add_row(*x)

        return table

    @property
    def _bomb_chords(self) -> list:
        return self.__bomb_chords

    @property
    def _field(self) -> list:
        return self.__field
    
    @property
    def _field_rich(self) -> Table:
        COLORS = {'?': 'grey_70', 'X': 'bright_red', ' ': 'white', '1': 'blue', '2': 'green', '3': 'red', '4': 'dark_blue', '5': 'dark_red', '6': 'cyan', '7': 'grey_60', '8': 'grey_50'}

        table = Table(title=self.__difficulty, box=box.HEAVY_EDGE, show_header=False, show_lines=True)

        for i in range(self.__width):
            y = Text(str(self.__width - i), '')
            row = list(Text(str(item), f'{COLORS[item]}') for item in self.__field[i])

            table.add_row(y, *row)

        x = list(Text(str(item)) for item in range(self.__width + 1))
        table.add_row(*x)

        return table

if __name__ == '__main__':
    with console.status("Carregando...", spinner="aesthetic"):
        fm = FieldManager()
        fm.generate(difficulty='difícil')

    console.rule('Minesweeper', characters='=')
    fm.play()
