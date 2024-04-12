import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sideways Shooter")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the ship
ship_image = pygame.image.load("images/ship.bmp")
ship_rect = ship_image.get_rect()
ship_rect.center = (50, SCREEN_HEIGHT // 2)

# Set up the bullet
bullet_image = pygame.Surface((10, 5))
bullet_image.fill(WHITE)
bullet_list = []

# Set up the alien
alien_image = pygame.image.load("images/alien.bmp")
alien_rect = alien_image.get_rect()

# Set up the clock
clock = pygame.time.Clock()

# Function to spawn a new alien
def spawn_alien():
    new_alien = alien_rect.copy()
    new_alien.x = SCREEN_WIDTH
    new_alien.y = random.randint(0, SCREEN_HEIGHT - alien_rect.height)
    return new_alien

# List to hold aliens
alien_list = []

# Main game loop
while True:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_rect = bullet_image.get_rect()
                bullet_rect.midleft = ship_rect.midright
                bullet_list.append(bullet_rect)

    # Move the ship up and down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ship_rect.top > 0:
        ship_rect.y -= 5
    if keys[pygame.K_DOWN] and ship_rect.bottom < SCREEN_HEIGHT:
        ship_rect.y += 5

    # Move the bullets
    for bullet in bullet_list:
        bullet.x += 7

    # Delete bullets that go off-screen
    bullet_list = [bullet for bullet in bullet_list if bullet.right < SCREEN_WIDTH]

    # Spawn new aliens randomly
    if random.randint(0, 100) < 2:
        alien_list.append(spawn_alien())

    # Move and draw the aliens
    for alien in alien_list:
        alien.x -= 3
        screen.blit(alien_image, alien)
        if alien.colliderect(ship_rect):
            pygame.quit()
            sys.exit()

    # Collision detection for bullets and aliens
    for bullet in bullet_list:
        for alien in alien_list:
            if bullet.colliderect(alien):
                bullet_list.remove(bullet)
                alien_list.remove(alien)

    # Draw the ship
    screen.blit(ship_image, ship_rect)

    # Draw the bullets
    for bullet in bullet_list:
        screen.blit(bullet_image, bullet)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
