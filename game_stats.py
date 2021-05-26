class GameStats():
    """Monitoring game statistics"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize stats is being changed during a game"""
        self.ships_left = self.settings.ship_limit
