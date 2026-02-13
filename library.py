from random import randrange

class FieldManager:
    def __init__(self, width: int, density_percentage: int) -> None:
        self.__width = width #height também
        self.__size = width * width
        self.__density = density_percentage / 100 #forma decimal
        self.__bombs = int(round(self.__density * self.__size))
        self.__bomb_chords = []
        self.__field = []
        self.__play_field = []

    def __repr__(self) -> str:
        return f'width: {self.__width}\nsize: {self.__size}\ndensity: {self.__density}\nbombs: {self.__bombs}\n{self.__bomb_chords}\nCampo:\n{self.__real_field_repr}\nCampo em jogo:\n{self.play_field}'
    
    def play(self) -> None:
        playing = True
        while playing:
            print(self.play_field)

            try:
                x = int(input('x: ').strip())
                y = int(input('y: ').strip())
            except ValueError:
                continue

            if x > self.width or y > self.width:
                print('out of range')
                continue
            
            playing = self.guess(x, y)

    def generate(self):
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

    def guess(self, x: int, y: int) -> bool:
        #coordenadas visuais, n reais
        real_y = self.__width - y
        real_x = x - 1
        tile = self.__field[real_y][real_x]

        if tile == 'X':
            self.game_over()
            return False
        elif tile != '0':
            self.__play_field[real_y][real_x] = self.__field[real_y][real_x]
            return True
        
        self.__play_field[real_y][real_x] = self.__field[real_y][real_x]
        return True

    def game_over(self) -> None:
        #fazer uma animação top, do campo revelando em cascata
        print('\nGame over\n')

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
    def play_field(self) -> str:
        f_str = ''
        y = self.__width

        for row in self.__play_field:
            gap = ' ' if y < 10 else ''
            f_str += gap + str(y) + ' '  + str(row) + '\n'
            y -= 1

        f_str += '     1'
        for x in range(2, self.__width + 1):
            f_str += '    ' + str(x)

        return '\n' + f_str

    @property
    def __real_field_repr(self) -> str:
        f_str = ''
        y = self.__width

        for row in self.__field:
            gap = ' ' if y < 10 else ''
            f_str += gap + str(y) + ' '  + str(row) + '\n'
            y -= 1

        f_str += '     1'
        for x in range(2, self.__width + 1):
            f_str += '    ' + str(x)

        return '\n' + f_str

if __name__ == '__main__':
    game = FieldManager(10, 20)
    game.generate()


    game.play()
