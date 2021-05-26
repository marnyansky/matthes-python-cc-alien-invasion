import pygame.font


class Button():
    """Allows to add 'Play' button to the game"""

    def __init__(self, ai_game, msg):
        """Initialize button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set size and features of buttons
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Ariel', 48)

        # Build rect object of the button and place it in the center of the game screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # One-time button message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Transforms msg into rectangle and align text to the center"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Display an empty button and display a message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
