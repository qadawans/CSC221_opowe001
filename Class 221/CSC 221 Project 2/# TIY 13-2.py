import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN_SIZE = (WIDTH, HEIGHT)

# Number of stars
NUM_STARS = 100

# Load star image
star_img = pygame.image.load('images/star.jpg')

# Initialize the screen
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Random Stars")

# Function to draw a star
def draw_star(screen, star_image, position):
    screen.blit(star_image, position)

# Generate random stars
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_STARS)]

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw stars
    for star in stars:
        draw_star(screen, star_img, star)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
