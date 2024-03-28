# TIY 12-1
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width = 800
height = 600

# Create the window
window = pygame.display.set_mode((width, height))

# Set the background color
blue = (0, 0, 255)
window.fill(blue)

# Update the display
pygame.display.update()

# Main loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
