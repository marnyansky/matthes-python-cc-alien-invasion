import pygame


class Ship():
    """Class for managing a spaceship"""

    def __init__(self, ai_game):
        """Game appereance and game settings"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        """Initial position of the spaceship"""
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        """Saving the real (вещественной) coordinate of the center of the spaceship"""
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates spaceship position depending on flag value (True/False)"""
        if self.moving_right and self.rect.right < self.screen_rect.right:  # attribute x is being updated, not rect ||| screen limits shouldn't be exceeded!
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:  # not elif block, because spaceship will always move to the right
            self.x -= self.settings.ship_speed

        # updating attribute rect based on self.x
        self.rect.x = self.x

    def blitme(self):
        """Draws a spaceship in a current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Places spaceship in the center of bottom screen limit"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
