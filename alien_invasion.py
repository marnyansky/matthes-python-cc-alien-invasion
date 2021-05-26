import sys

import pygame

from alien import Alien
from bullet import Bullet
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
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()

    # utils

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ~mouse click on window button [X] or pressing Alt + F4
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Handles pressing keys"""
        if event.key == pygame.K_RIGHT:  # if right arrow => key is pressed
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:  # replacement of pygame.K_q
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Handles releasing keys"""
        if event.key == pygame.K_RIGHT:  # if right arrow => key is released
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        """Create invasion fleet"""
        # Create an alien and calculate possible number of aliens in a row
        # Interval between neighboring aliens = alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Calculate number of rows of aliens could be placed on a screen"""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create invasion fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):  # alien_number = alien_id
        # Create an alien and place him in a row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _fire_bullet(self):
        """Creating a new bullet (rocket) and including it in 'bullets' group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet positions and remove fired bullets"""
        # Update bullet positions
        self.bullets.update()

        # Remove bullets reached coord y=0 (top border of the game screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets)) # manual check of amount of bullets

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # for bullet in bullets.sprites(): # TODO fix
        #     bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
