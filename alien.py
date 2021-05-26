import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing a single alien"""

    def __init__(self, ai_game):
        """Initialize an alien and set his initial position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image and set 'rect' attribute
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Every new alien appears in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save exact horizontal position of an alien
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns True if alien is at the screen border"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Moves an alien to the right and to the left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
