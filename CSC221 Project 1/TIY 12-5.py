import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("You pressed the spacebar.")
    
    # Fill the screen with a color
    screen.fill((255, 255, 255))  # White 
    
    # Update the display
    pygame.display.flip()

pygame.quit()
