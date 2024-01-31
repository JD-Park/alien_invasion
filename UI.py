import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the main window
width, height = 800, 600

# Create the main window
main_window = pygame.display.set_mode((width, height))

# Set the dimensions of the options window
options_width, options_height = 300, 200

# Create the options window
options_window = pygame.display.set_mode((options_width, options_height), pygame.NOFRAME)

# Draw the options window background
options_window.fill((255, 255, 255))

# Draw the options window contents
# ...

# Update the options window
pygame.display.flip()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input for the options window
    # ...

    # Update the options window
    pygame.display.flip()

# Quit Pygame
pygame.quit()