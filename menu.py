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
        self.button_x = self.setting.screen_width - self.width
        self.button_y = self.setting.screen_height - self.height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.br = pygame.Rect(self.button_x, self.button_y, self.width, self.height)
        self.rect.center = self.screen_rect.center

        """The button message."""
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn message into rendered image."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # self.msg_image_rect =  self.msg_image.get_rect()
        # self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw the message."""
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    # def draw_button_br(self):
    #     """Draw blank button and then draw the message."""
    #     self.msg_image_rect = self.msg_image.get_rect()
    #     self.msg_image_rect.center = self.br.center
    #     self.screen.fill(self.button_color, self.br)
    #     self.screen.blit(self.msg_image, self.msg_image_rect)

    # def update(self, msg):
    #     self._prep_msg(msg)
    #     # self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
    #     # self.rect = pygame.Rect(button_x, button_y, self.width, self.height)
    #     self.draw_button_br()


class StartScreen:
    """A class to manage the start screen."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/tmpogs02nuw.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class GameScreen:
    """A class to manage the start screen."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/tmpvtw6n17l.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Title:
    """A class to manage the start screen."""

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        self.text_color = '#F2B31C'
        self.font = pygame.font.SysFont("Arial", 192)
        
        """The button message."""
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn message into rendered image."""
        self.msg_image = self.font.render(msg, True, self.text_color)

    def blitme(self):
        """Draw blank button and then draw the message."""
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (960, 300)
        self.screen.blit(self.msg_image, self.msg_image_rect)
