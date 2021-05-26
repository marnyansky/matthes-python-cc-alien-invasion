import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing a single alien"""

    def __init__(self, ai_game):
        """Initialize an alien and set his initial position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load alien image and set 'rect' attribute
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Every new alien appears in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save exact horizontal position of an alien
        self.x = float(self.rect.x)
