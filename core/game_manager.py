from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..ui.table_renderer import TableRenderer
    from ..ui.input_handler import InputHandler
    from ..ui.ui_handler import UiHandler
    from field_manager import FieldManager

class GameManager():
    def __init__(self, fm: FieldManager, tr: TableRenderer, ih: InputHandler, uh: UiHandler):
        self.fm = fm
        self.tr = tr
        self.ih = ih
        self.uh = uh

    def start(self):
        self.uh.intro()
        self.mainloop()

    def mainloop(self):
        while True:
            action = self.choose_action()

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
        self.uh.display_difficulty()
        diff = self.ih.prompt_difficulty()

        if diff != 5:
            CHART = {1: 'fácil', 2: 'médio', 3: 'difícil', 4: 'insano'}
            self.fm.generate_basic_data(difficulty=CHART.get(diff, 'médio'))
        else:
            #self.fm.generate_basic_data(*self.ih.personal_difficulty())
            pass

        self.tr.render_visible_field(self.fm.render_data)
        self.fm.first_guess(*self.ih.prompt_chords(self.fm.width))

        while True:
            self.tr.render_visible_field(self.fm.render_data)
            break

    def win():
        pass

    def lose():
        pass

    def choose_action(self) -> int:
        self.uh.display_options()
        return self.ih.prompt_options()

    def tutorial(self):
        pass