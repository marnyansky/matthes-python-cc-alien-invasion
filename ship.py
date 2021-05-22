import pygame


class Ship():
    """Class for managing a spaceship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        """Initial position of the spaceship"""
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates spaceship position depending on flag value (True/False)"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:  # not elif block: spaceship will always move to the right
            self.rect.x -= 1

    def blitme(self):
        """Draws a spaceship in a current position"""
        self.screen.blit(self.image, self.rect)
