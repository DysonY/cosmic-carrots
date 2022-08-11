from curses import *


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 24


class Game:
    def __init__(self, screen):
        self.screen = screen
        screen.clear()
        screen.refresh()


    def draw(self, screen):
        self._draw_topbar(screen)
        self._draw_map(screen)
        self._draw_location_info(screen)
        screen.refresh()


    def _draw_topbar(self, screen):
        screen.addstr(0, 0,  '1. Journey',  A_UNDERLINE | A_BOLD)
        screen.addstr(0, 18, '2. Vessel',   A_UNDERLINE | A_BOLD)
        screen.addstr(0, 35, '3. Crew',     A_UNDERLINE | A_BOLD)
        screen.addstr(0, 50, '4. Supplies', A_UNDERLINE | A_BOLD)
        screen.addstr(0, 70, '5. Log',      A_UNDERLINE | A_BOLD)


    def _draw_map(self, screen):
        for i in range(1, SCREEN_HEIGHT - 2):
            screen.addstr(i, 0, '.' * SCREEN_WIDTH)
        screen.addstr(SCREEN_HEIGHT - 2, 0, '_' * SCREEN_WIDTH)


    def _draw_location_info(self, screen):
        # TODO add info bar on last line below the map
        pass


def main(screen):
    game = Game(screen)
    game.draw(screen)

    while True:
        ch = screen.getch()
        if ch == 127: break


if __name__ == '__main__':
    wrapper(main)

