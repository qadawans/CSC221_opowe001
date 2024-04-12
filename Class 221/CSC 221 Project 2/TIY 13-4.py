import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN_SIZE = (WIDTH, HEIGHT)

# Number of raindrops and size range
NUM_RAINDROPS = 100
RAINDROP_SIZE = 5
RAINDROP_SPEED = 3

# Load raindrop image
raindrop_img = pygame.image.load('images/raindrop.jpg')
raindrop_img = pygame.transform.scale(raindrop_img, (RAINDROP_SIZE, RAINDROP_SIZE))

# Initialize the screen
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Falling Raindrops")

# Function to draw a raindrop
def draw_raindrop(screen, raindrop_image, position):
    screen.blit(raindrop_image, position)

# Generate random raindrops
raindrops = [(random.randint(0, WIDTH), random.randint(-HEIGHT, 0)) for _ in range(NUM_RAINDROPS)]

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw and update raindrops
    for i, raindrop in enumerate(raindrops):
        draw_raindrop(screen, raindrop_img, raindrop)
        x, y = raindrop
        y += RAINDROP_SPEED
        raindrops[i] = (x, y)

        # Respawn raindrop if it goes off the screen
        if y > HEIGHT:
            raindrops[i] = (random.randint(0, WIDTH), random.randint(-HEIGHT, 0))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit frame rate to 60 FPS

# Quit Pygame
pygame.quit()
