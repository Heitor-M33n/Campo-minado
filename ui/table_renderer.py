from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich import box

class TableRenderer():
    COLORS = {'?': 'grey_70', 'X': 'bright_red', ' ': 'white', '1': 'blue', '2': 'green', '3': 'red', '4': 'dark_blue', '5': 'dark_red', '6': 'cyan', '7': 'grey_60', '8': 'grey_50'}
    REPLACES = {'X': '💣', 'F': '🚩'}

    def __init__(self, console: Console):
        self.console = console

    def render_field(self, render_data: dict) -> None:
        self.console.print(self.__generate_table(render_data, render_data['field']))
    
    def render_visible_field(self, render_data: dict) -> Table:
        self.console.print(self.__generate_table(render_data, render_data['visible_field']))

    def __generate_table(self, render_data: dict, field: list) -> Table:
        table = Table(title=f"Dificuldade: {render_data['difficulty'].title()} - {render_data['bombs']} bombas", box=box.HEAVY_EDGE, show_header=False, show_lines=True)
        table_field = []

        for row in field:
            new_row = []

            for item in row:
                new_row.append(TableRenderer.REPLACES.get(item, item))

            table_field.append(new_row)                

        for i in range(render_data['width']):
            y = Text(str(render_data['width'] - i), '')
            row = list(Text(str(item), f'{TableRenderer.COLORS.get(item, '')}') for item in table_field[i])

            table.add_row(y, *row)

        x = list(Text(str(item)) for item in range(render_data['width'] + 1))
        table.add_row(*x)

        return table