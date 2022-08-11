from curses import *

import sys


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 24

# put into utils.py?
def restrict(n, _max):
    if n < 0: return 0
    if n > _max: return _max
    return n


class Game:
    def __init__(self, screen):
        self.screen = screen
        screen.clear()
        screen.refresh()

        self.menu_idx = 0
        self.menu_fns = [ self._draw_journey, self._draw_vessel,
                          self._draw_crew,    self._draw_supplies,
                          self._draw_log ]

        self.selection_indices = [ 0 for _ in range(20) ]
        # TODO read from settings file
        # each list entry corresponds to a menu_idx value
        self.max_selections = [ 0, 3, 20, 20, 20, 4 ]


    def draw(self):
        self._draw_topbar()
        self.menu_fns[self.menu_idx]()
        self._draw_location_info()
        self.screen.refresh()


    def _draw_topbar(self):
        self.screen.addstr(0, 0,  '1. Journey',  A_UNDERLINE | A_BOLD)
        self.screen.addstr(0, 18, '2. Vessel',   A_UNDERLINE | A_BOLD)
        self.screen.addstr(0, 35, '3. Crew',     A_UNDERLINE | A_BOLD)
        self.screen.addstr(0, 50, '4. Supplies', A_UNDERLINE | A_BOLD)
        self.screen.addstr(0, 70, '5. Log',      A_UNDERLINE | A_BOLD)


    def _draw_journey(self):
        for i in range(1, SCREEN_HEIGHT - 2):
            self.screen.addstr(i, 0, '.' * SCREEN_WIDTH)
        self.screen.addstr(SCREEN_HEIGHT - 2, 0, '_' * SCREEN_WIDTH)


    def _draw_vessel(self):
        self._draw_vessel_submenu()


    def _draw_vessel_submenu(self):
        self.screen.addstr(9,  33, 'Component Info')
        self.screen.addstr(10, 33, 'Allocate Power')
        self.screen.addstr(11, 33, 'Repair')
        self.screen.addstr(12, 33, 'Delegate Task')

        for i in range(9, 13):
            self.screen.addch(i, 31, ' ')
        self.screen.addch(9 + self.selection_indices[self.menu_idx], 31, '>')


    def _draw_crew(self):
        # TODO
        pass


    def _draw_supplies(self):
        # TODO
        pass


    def _draw_log(self):
        # TODO
        pass


    def _draw_location_info(self):
        # TODO add info bar on last line below the map
        pass


    def handle_key(self):
        ch = self.screen.getch()
        if ch == 127:
            sys.exit()
        elif ch > 48 and ch < 54:
            self._handle_menu(ch)
        elif ch == KEY_UP or ch == KEY_DOWN:
            self._handle_selection(ch)


    def _handle_menu(self, ch):
        # TODO block call under certain conditions? e.g. if dialogue or event
        # window is open
        self._clear_screen()
        self.menu_idx = ch - 49


    def _clear_screen(self):
        for i in range(1, SCREEN_HEIGHT - 2):
            self.screen.addstr(i, 0, ' ' * SCREEN_WIDTH)


    def _handle_selection(self, ch):
        if ch == KEY_UP:
            delta = -1
        else:
            delta = 1

        new_sel = restrict(self.selection_indices[self.menu_idx] + delta,
                           self.max_selections[self.menu_idx])
        self.selection_indices[self.menu_idx] = new_sel


def main(screen):
    curs_set(0) # hide cursor
    game = Game(screen)
    game.draw()

    while True:
        game.handle_key()
        game.draw()


if __name__ == '__main__':
    wrapper(main)

