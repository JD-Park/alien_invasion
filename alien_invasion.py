import sys
import pygame
import bullet
import ship
import alien
import settings
import games_stats
import menu

from time import sleep

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """Initialize the game, and create instances of classes."""
        pygame.init()
        self.settings = settings.Settings()
    
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.stats = games_stats.GameStats(self)
        self.menu = menu.StartScreen(self)
        self.ship = ship.Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bullet = bullet.Bullet(self)
        self.aliens = pygame.sprite.Group()
        self.alien = alien.Alien(self)
        # self.firing = self.bullet.firing
        # self.count = self.bullet.count

        self._create_fleet()

        """Set background color."""
        self.bg_color = self.settings.bg_color

        """Create play button."""
        self.play_button = menu.Button(self, "Play")
        
    def run_game(self): 
        """Start the main loop for the game."""
        while True:
            """Watch for keyboard and mouse events from helper method."""
            self._check_events()
               
            if self.stats.game_active:
                """Move ship."""
                self.ship.update()

                """Move bullets."""
                self.bullets.update()

                """Remove bullets."""
                bullet.Bullet.remove_bullet(self)

                """Update the alien fleet."""
                self._check_edges()
                self.aliens.update()
                self._new_fleet()

                """Check for collisions or invasion."""
                pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
                if pygame.sprite.spritecollideany(self.ship, self.aliens):
                    self._ship_hit()
                    # print("Ship hit!!!")
                self._alien_invades()

            """Redraw the screen based on helper method."""
            self._update_screen()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1  
            self.bullets.empty()     
            self.aliens.empty()       
            self._create_fleet()        
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
    
    def _alien_invades(self):
        """Respond to a succesful alien invasion."""
        screen_rect = self.screen.get_rect()
        for new_alien in self.aliens.sprites():
            if new_alien.rect.bottom == screen_rect.bottom:
                self._ship_hit()
                break

    def _create_fleet(self):
        """Create a fleet of aliens."""
        new_alien = alien.Alien(self)
        """Determine number of aliens per row in the fleet."""
        alien_width, alien_height = new_alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Determine number of rows that fit on the screen."""        
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows =  available_space_y // (2 * alien_height)

        """Create additional rows."""
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                new_alien = alien.Alien(self)
                new_alien.x = alien_width + 2 * alien_width * alien_number
                new_alien.rect.x = new_alien.x
                new_alien.rect.y = alien_height + 2 * new_alien.rect.height * row_number 
                self.aliens.add(new_alien)
    
    def _check_edges(self):
        """Check edges."""
        for new_alien in self.aliens.sprites():
            if new_alien.check_edges():
                alien.Alien.change_fleet_direction(self)
                break
    
    def _new_fleet(self):
        """Create new fleet after current one is destroyed."""
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
      
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    """Move ship left and right."""
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                    """Quit game when 'q' is pressed."""
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    bullet.Bullet.fire_bullet(self)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    """Move ship left and right."""
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_SPACE:
                    self.firing = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
   
    def _check_play_button(self, mouse_pos):
        """Start the game when play button is clicked."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        """Draw the menu buttons."""
        if not self.stats.game_active:
            self.menu.blitme()
            self.play_button.draw_button()
        
        else:
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)



        """Make the most recently drawn screen visible."""
        pygame.display.flip()
        
if __name__ == '__main__':
    """Make a game instance, and run the game."""
    ai = AlienInvasion()
    ai.run_game()