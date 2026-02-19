from random import randrange

class FieldManager:
    def __init__(self) -> None:
        self.clear()

    def clear(self) -> None:
        self.__difficulty = ''
        self.__width = 0
        self.__size = 0
        self.__density = 0
        self.__bombs = 0
        self.__bomb_chords = []
        self.__field = []
        self.__visible_field = []

    def reveal(self, x: int, y: int) -> None:
        y = self.__width - y
        x -= 1

        if self.__visible_field[y][x] == 'F':
            return
        elif self.__visible_field[y][x] != ' ':
            self.__visible_field[y][x] = self.__field[y][x]

        blank_tiles = [[y, x]]
        for y, x in blank_tiles:
            for i in range(-1, 2):
                for c in range(-1, 2):
                    if y + i in range(0, self.__width) and x + c in range(0, self.__width) and self.__field[y + i][x + c] == ' ' and ([y + i, x + c] not in blank_tiles):
                        blank_tiles.append([y + i, x + c])

        close_tiles = []
        for y, x in blank_tiles:
            for i in range(-1, 2):
                for c in range(-1, 2):
                    if y + i in range(0, self.__width) and x + c in range(0, self.__width) and [y + i, x + c] not in blank_tiles and [y + i, x + c] not in close_tiles:
                        close_tiles.append([y + i, x + c])

        for y, x in blank_tiles + close_tiles:
            self.__visible_field[y][x] = self.__field[y][x] if self.__visible_field[y][x] != 'F' else 'F'

    def flag(self, x: int, y: int) -> None:
        y = self.__width - y
        x -= 1

        tile = self.__visible_field[y][x]

        if tile == '?':
            self.__visible_field[y][x] = 'F'
        elif tile == 'F':
            self.__visible_field[y][x] = '?'

    def first_guess(self, x: int, y: int) -> None:
        self.__generate_field(x, y)
        self.reveal(x, y)

    def generate_basic_data(self, width: int = 0, density_percentage: int = 0, difficulty: str = '') -> None:
        DIFF_CHART = {'fácil': (5, 15), 'médio': (8, 20), 'difícil': (10, 25), 'insano': (15, 35)}

        self.clear()

        if not difficulty:
            self.__width = width
            self.__density = density_percentage / 100
            self.__difficulty = 'personalizado'
        else:
            self.__width = DIFF_CHART[difficulty.lower()][0]
            self.__density = DIFF_CHART[difficulty.lower()][1] / 100
            self.__difficulty = difficulty.lower()

        self.__size = self.__width * self.__width
        self.__bombs = int(round(self.__density * self.__size))

        for y in range(self.__width):
            self.__visible_field.append([])
            for _ in range(self.__width):
                self.__visible_field[y].append('?')

    def __generate_field(self, guess_x: int, guess_y: int) -> None:
        #gerar coordenadas das bombas, evitando o first guess
        safe_chords = [[guess_y, guess_x]]
        for i in range(-1, 2):
            for c in range(-1, 2):
                if guess_y + i in range(1, self.__width + 1) and guess_x + c in range(1, self.__width + 1) and [guess_y + i, guess_x + c] not in safe_chords:
                    safe_chords.append([guess_y + i, guess_x + c])

        for _ in range(self.__bombs):
            while True:
                x, y = randrange(self.__width), randrange(self.__width)
                x += 1
                y += 1
                if [x, y] not in self.__bomb_chords + safe_chords:
                    self.__bomb_chords.append([x, y])
                    break

        #gerar matriz
        for y in range(self.__width):
            self.__field.append([])
            for _ in range(self.__width):
                self.__field[y].append('')

        #posicionar bombas usando coordenadas do plano cartesiano
        for y in range(self.__width):
            for x in range(self.__width):
                if [x + 1, self.__width - y] in self.__bomb_chords:
                    self.__field[y][x] = 'X'

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

    @property
    def width(self) -> int:
        return self.__width

    @property
    def flagged_field(self) -> list:
        flagged_field = []

        for r in self.__field:
            row = []

            for item in r:
                if item == 'X':
                    item = 'F'
                row.append(item)

            flagged_field.append(row)

        return flagged_field
    
    @property
    def flagged_blanks_visible_field(self) -> list:
        flagged_field = []

        for r in self.__visible_field:
            row = []

            for item in r:
                if item == '?':
                    item = 'F'
                row.append(item)

            flagged_field.append(row)

        return flagged_field
    
    @property
    def render_data(self) -> dict:
        return {'difficulty': self.__difficulty, 'width': self.__width, 'bombs': self.__bombs, 'field': self.__field, 'visible_field': self.__visible_field}
    
    def __repr__(self) -> str:
        return f'difficulty: {self.__difficulty}\nwidth: {self.__width}\nsize: {self.__size}\ndensity: {self.__density}\nbombs: {self.__bombs}\nbomb_chords: {self.__bomb_chords}\nfield:\n{self.__field}\nplay_field:\n{self.visible_field}'