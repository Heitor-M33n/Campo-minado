from rich.prompt import Prompt

#nada funciona aqui por enquanto, só transferi as funções do field_manager, necessita de uma correção pesada

class Game_manager():
    def __init__(self, console, fm, tr):
        self.console = console
        self.fm = fm
        self.tr = tr

    def mainloop():
        pass

    def run(self) -> None:
        pass

    def play(self) -> None:
        console = self.console

        playing = True
        mode = 'guess'

        console.print(self.play_field_rich)

        while playing:
            mode = Prompt.ask('Modo?', choices=('flag', 'guess'), default=mode)
            x = int(Prompt.ask('Insira a coordenada X', choices=list(str(item) for item in range(1, self.__width + 1)), show_choices=False))
            y = int(Prompt.ask('Insira a coordenada Y', choices=list(str(item) for item in range(1, self.__width + 1)), show_choices=False))

            playing = self.guess(x, y, mode)

            console.clear()
            console.print(self.play_field_rich)

            if self._flagged_blanks_play_field == self._flagged_field:
                self.win()
                break

        if not playing:
            self.game_over()

    def guess(self, visual_x: int, visual_y: int, mode: str) -> bool:
        console = self.console

        real_y = self.__width - visual_y
        real_x = visual_x - 1
        tile = self.__field[real_y][real_x]

        if self.__visible_field[real_y][real_x] not in ('🚩', '?'):
            return True

        if mode == 'guess':
            if tile == 'X':
                self.__visible_field[real_y][real_x] = '💣'
                return False
            elif tile != ' ':
                self.__visible_field[real_y][real_x] = tile
                return True
            
            blank_tiles = [[real_y, real_x]]
            appended = True
            while appended:
                appended = False

                for y, x in blank_tiles:
                    for i in range(-1, 2):
                        for c in range(-1, 2):
                            if y + i in range(0, self.__width) and x + c in range(0, self.__width) and self.__field[y + i][x + c] == ' ' and ([y + i, x + c] not in blank_tiles):
                                blank_tiles.append([y + i, x + c])
                                appended = True

            close_tiles = []
            for y, x in blank_tiles:
                for i in range(-1, 2):
                    for c in range(-1, 2):
                        if y + i in range(0, self.__width) and x + c in range(0, self.__width) and [y + i, x + c] not in blank_tiles and [y + i, x + c] not in close_tiles:
                            close_tiles.append([y + i, x + c])

            for y, x in blank_tiles + close_tiles:
                self.__visible_field[y][x] = self.__field[y][x]

            return True
        
        elif mode == 'flag':
            if self.__visible_field[real_y][real_x] == 'F':
                self.__visible_field[real_y][real_x] = '?'
            elif self.__visible_field[real_y][real_x] != '?':
                pass
            else:
                self.__visible_field[real_y][real_x] = 'F'

            return True

    def game_over(self) -> None:
        console = self.console

        #fazer uma animação top, do campo revelando em cascata
        console.print('\nGame over\n')

    def win(self) -> None:
        console = self.console

        console.print('\nVocê venceu!\n')