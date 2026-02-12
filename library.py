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
                if f'{x}, {y}' not in self.__bomb_chords:
                    self.__bomb_chords.append(f'{x}, {y}')
                    break

        #gerar matriz
        for x in range(self.__width):
            self.__field.append([])
            for _ in range(self.__width):
                self.__field[x].append('')

        #posicionar bombas
        for x in range(self.__width):
            for y in range(self.__width):
                if f'{x}, {y}' in self.__bomb_chords:
                    self.__field[x][y] = 'X'

        #gerar demais tiles
        for x in range(self.__width):
            for y in range(self.__width):
                if self.__field[x][y] == 'X':
                    continue
                
                #descobrir número
                bombs = 0
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if 0 <= x + a < self.__width and 0 <= y + b < self.__width and self.__field[x + a][y + b] == 'X':
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

field = FieldManager(10, 20)
field.generate()

print(field)