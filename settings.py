class Settings:
    """Class containing all settings of the game"""

    def __init__(self):
        """Screen settings"""
        self.screen_width = 1200  # if window mode is selected
        self.screen_height = 800  # if window mode is selected
        self.bg_color = (0, 0, 0)  # 82, 94, 84

        """Spaceship settings"""
        self.ship_speed = 1.5

        """Bullet (rocket) settings"""
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 3
