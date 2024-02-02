import pygame.font

from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """A class to handle the scoreboard."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        """Font settings."""
        self.text_color = '#000000'
        self.font = pygame.font.SysFont(None, 48)

        """Prepare the score image."""
        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, 
                                            self.text_color, self.settings.bg_color)
        
        """Display the score at the top right of the screen."""
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """Turn the level into a redered image."""
        self.level_str = str(self.stats.level)
        self.level_image = self.font.render(self.level_str, True,
                                            self.text_color, self.settings.bg_color)
        
        """Position the level below the score."""
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_highscore(self):
        """Turn high score into a rendered image."""
        hs = round(self.stats.high_score, -1)
        hs_str = "{:,}".format(hs)
        self.hs_image = self.font.render(hs_str, True, 
                                         self.text_color, self.settings.bg_color)
        
        """Center the high score at the top of the top of the screen."""
        self.hs_rect = self.hs_image.get_rect()
        self.hs_rect.centerx = self.screen_rect.centerx
        self.hs_rect.top = self.screen_rect.top

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw the score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hs_image, self.hs_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_hs(self):
        """Check current score vs high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_highscore()