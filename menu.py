import pygame
import pygame.font

class Button:
    """A class to manage buttons."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """Set dimensions and properties of the button."""
        self.width, self.height = 200, 50
        self.button_color = '#F2B31C'
        self.text_color = '#000000'
        self.font = pygame.font.SysFont(None, 48)

        """Build the button's rect object and center it."""
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        """The button message."""
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn message into rendered image."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect =  self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw the message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class StartScreen:
    """A class to manage the start screen."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/tmpogs02nuw.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)