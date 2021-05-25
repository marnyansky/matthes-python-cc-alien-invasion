import pygame

from pygame.sprite import Sprite, AbstractGroup


class Bullet(Sprite):
    """Class for bullet (spaceship weaponry) management"""

    def __init__(self, ai_game, *groups: AbstractGroup):
        """Creating a bullet object in current spaceship position"""
        super().__init__(*groups)
        self.screen = ai_game.screen
        self.settings = ai_game.setings
        self.color = self.settings.bullet_color

        # Creating a bullet (rocket) in position (0, 0) and assign a right position for it
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Keeping bullet (rocket position) in a real (вещественном) format
        self.y = float(self.rect.y)

    def update(self):
        """Moving bullet (rocket) up: 'firing' a shot"""
        # Updating bullet (rocket) position in real (вещественном) format
        self.y -= self.settings.bullet_speed
        # Updating position of a bullet rectangle # TODO understand difference: self.y, self.rect.y
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
