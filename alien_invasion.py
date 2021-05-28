import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
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

        # Create instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self._create_fleet()

        # Create 'Play' button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Launch of main game process (loop)"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                # self.bullets.update() TODO: check: included or not
                self._update_bullets()
                self._update_aliens()

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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

    def _check_play_button(self, mouse_pos):
        # TODO: add option start a new game by pressing 'p'/'P' key: book: page 299, task 14.1
        """Launches a new game on click on 'Play' button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset game stats
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True

            # Clear the list of aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new invasion fleet and place spaceship in the center
            self._create_fleet()
            self.ship.center_ship()

            # Hide mouse cursor # TODO: allow to show mouse cursor (in window mode!) via options
            pygame.mouse.set_visible(False)

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

    # def _check_fleet_edges(ai, aliens):
    #     """Responds to event 'alien is reached screen limit' """
    #     for alien in aliens.sprites():
    #         if alien.check_edges(): # TODO fix
    #             _change_fleet_direction(ai, aliens)
    #             break

    def _change_fleet_direction(self):
        """Moves down the whole fleet and changes its move direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

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

    def _update_aliens(self):
        """Checks if fleet is reached screen limit,
            with further updating positions of all aliens of the invasion fleet"""
        # self._check_fleet_edges() # TODO fix method first
        self.aliens.update()

        # Check collisions between spaceship and aliens
        # if pygame.sprite.spritecollideany(self.ship, self.aliens): # TODO fix method first
        #     self._ship_hit()

        # Check if alien(s) reached the bottom of the game screen
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Checks if alien(s) reached the bottom of the game screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Happens the same as if alien collided with a spaceship
                self._ship_hit()
                break

    def _ship_hit(self):
        """Handles collision between spaceship and an alien"""
        if self.stats.ships_left > 0:
            # Lowers value of 'ships_left'
            self.stats.ships_left -= 1

            # Clean lists of aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new invasion fleet and place spaceship in the center
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_bullets(self):
        """Update bullet positions and remove fired bullets"""
        # Update bullet positions
        self.bullets.update()

        # Remove bullets reached coord y=0 (top border of the game screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # TODO remove: print(len(self.bullets)) # manual check of amount of bullets
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Handle collisions featuring bullets and aliens"""
        # Remove bullets and aliens if they collided
        # Check if alien is hit: then remove the bullet and the alien from the game screen
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Remove existing bullets and create a new invasion fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # for bullet in self.bullets.sprites(): # TODO fix
        #     bullet.draw_bullet(bullet.image)
        self.aliens.draw(self.screen)

        # 'Play' button is displayed if the game is not active
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
