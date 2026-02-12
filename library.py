from random import randrange

class FieldManager:
    def __init__(self, width: int, density_percentage: int) -> None:
        self.__width = width #height também
        self.__size = width * width
        self.__density = density_percentage / 100 #forma decimal
        self.__bombs = int(round(self.__density * self.__size))
        self.__bomb_chords = []
        self.__field = []

    def __repr__(self) -> str:
        return f'width: {self.width}\nsize: {self.size}\ndensity: {self.density}\nbombs: {self.bombs}\n{self.bomb_chords}\nCampo:\n{self.field}'
    
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

                self.__field[x][y] = str(bombs)

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
    def bomb_chords(self) -> list:
        return self.__bomb_chords
    
    @property
    def field(self) -> str:
        f_str = ''
        for row in self.__field:
            f_str += str(row) + '\n'

        return f_str

if __name__ == '__main__':
    field = FieldManager(10, 4)
    field.generate()

    print(field)