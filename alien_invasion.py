import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class for resource management and game behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # window mode
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    # utils

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ~mouse click on window button [X]
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Handles pressing keys"""
        if event.key == pygame.K_RIGHT:  # if right arrow => key is pressed
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:  # replacement of pygame.K_q
            sys.exit()

    def _check_keyup_events(self, event):
        """Handles releasing keys"""
        if event.key == pygame.K_RIGHT:  # if right arrow => key is released
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
