import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired at the ship's current position."""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        """Create a bullet rect at (0,0) and then set correct position."""
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        """Store the bullet's position as a decimal value."""
        self.y = float(self.rect.y)

        """Auto fire flag."""
        # self.firing = False
        # self.count = 0

    def update(self):
        """Move the bullet up the screen."""
        """Update the decimal position of the bullet."""
        self.y -= self.settings.bullet_speed
        """Update the rect position."""
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            # self.count += 1
            # print(len(self.bullets))

    def remove_bullet(self):
        """Remove bullet after it has passed offscreen."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                # print(len(self.bullets))