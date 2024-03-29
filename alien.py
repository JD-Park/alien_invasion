import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        """Load the alien image and set its rect attribute."""
        self.image = pygame.image.load('images/Alien.bmp')
        self.rect = self.image.get_rect()

        """Start each alien near the top of left of the screen."""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height/2

        """Store the alien's exact horizontal position."""
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return true if an alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        """Move the alien to the right."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def change_fleet_direction(self):
        """Drop entire fleet and change the fleets direction."""
        for new_alien in self.aliens.sprites():
            new_alien.rect.y += self.settings.drop_speed
        self.settings.fleet_direction *= -1

