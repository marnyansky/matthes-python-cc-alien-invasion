class GameStats():
    """Monitoring game statistics"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Game is launched while in active state
        self.game_active = False

    def reset_stats(self):
        """Initialize stats is being changed during a game"""
        self.ships_left = self.settings.ship_limit
