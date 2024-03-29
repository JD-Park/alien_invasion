import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        """Decimal value for ship speed."""
        self.x = float(self.rect.x)
        
        """Movement flag."""
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        # if self.moving_up:
        #     self.rect.
        # if self.moving_down:
        #     self.rect.

        """Update rect object from self.x"""
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def draw_lives(self):
        """Draw smaller ships to show remaining lives."""
        self.screen.blit(self.image2, self.rect)

    def center_ship(self):
        """Re-center the ship."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
