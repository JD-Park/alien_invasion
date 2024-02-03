class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        """Screen settings."""
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = '#0A1439'

        """Ship settings."""
        self.ship_speed = 1.5

        """Bullet settings."""
        self.bullet_width = 10
        self.bullet_height = 60
        self.bullet_color = '#00ff09'
        self.bullets_allowed = 3

        """Alien settings."""
        self.drop_speed = 10


        """Level settings."""
        # self.speed_scale = 2.0
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_limit = 3
        self.bullet_speed = 1.5
        self.alien_speed = 0.5

        """-1 = left; 1 = right."""
        self.fleet_direction = 1

        """Scoring."""
        self.alien_points = 50

    def increase_stats(self):
        """Increase speed based on level."""
        # self.ship_speed *= self.speed_scale
        # self.bullet_speed *= self.speed_scale
        # self.alien_speed *= self.speed_scale

        self.ship_speed += 0.1
        self.bullet_speed += 0.1
        self.alien_speed += 0.1
        self.alien_points += 50