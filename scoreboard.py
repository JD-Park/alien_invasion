import pygame.font

class Scoreboard:
    """A class to handle the scoreboard."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
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

    def show_score(self):
        """Draw the score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hs_image, self.hs_rect)

    def check_hs(self):
        """Check current score vs high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_highscore()