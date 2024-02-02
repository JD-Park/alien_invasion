class GameStats:
    """Track stats for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        """Start the game in an inactive state."""
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change durign the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0