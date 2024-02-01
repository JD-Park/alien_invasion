class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        """Screen settings."""
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = '#0A1439'

        """Ship settings."""
        self.ship_speed = 1.0
        self.ship_limit = 3

        """Bullet settings."""
        self.bullet_speed = 1.4
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = '#000000'
        self.bullets_allowed = 3

        """Alien settings."""
        self.alien_speed = 1
        self.drop_speed = 50
        """-1 = left; 1 = right."""
        self.fleet_direction = 1