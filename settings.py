class Settings:
    """Class containing all settings of the game"""

    def __init__(self):
        """Initialize static game settings"""
        """Screen settings"""
        self.screen_width = 1200  # if window mode is selected
        self.screen_height = 800  # if window mode is selected
        self.bg_color = (0, 0, 0)  # 82, 94, 84

        """Spaceship settings"""
        self.ship_speed = 1.5
        self.ship_limit = 3

        """Alien settings"""
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 equals moving to the right, and -1 - to the left
        self.fleet_direction = 1

        """Bullet (rocket) settings"""
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 3

        """Game acceleration on finishing the level"""
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that is changing during the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # fleet_direction = 1 for invasion fleet moving right; -1 for left
        self.fleet_direction = 1

    def increase_speed(self):
        """Settings aimed to increase the speed"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
