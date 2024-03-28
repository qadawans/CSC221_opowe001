import pygame
import sys
from pygame.locals import *

class RocketGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Rocket Game")
        self.clock = pygame.time.Clock()
        
        self.rocket_image = pygame.image.load("ship.bmp").convert_alpha()
        self.rocket_rect = self.rocket_image.get_rect()
        self.rocket_rect.center = (self.screen_width // 2, self.screen_height // 2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def move_rocket(self, dx, dy):
        self.rocket_rect.x += dx
        self.rocket_rect.y += dy

        # Make sure the rocket stays within the screen boundaries
        self.rocket_rect.x = max(0, min(self.rocket_rect.x, self.screen_width - self.rocket_rect.width))
        self.rocket_rect.y = max(0, min(self.rocket_rect.y, self.screen_height - self.rocket_rect.height))

    def run(self):
        while True:
            self.handle_events()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.move_rocket(0, -5)
            if keys[pygame.K_DOWN]:
                self.move_rocket(0, 5)
            if keys[pygame.K_LEFT]:
                self.move_rocket(-5, 0)
            if keys[pygame.K_RIGHT]:
                self.move_rocket(5, 0)

            self.screen.fill((255, 255, 255))  # Fill screen with white color
            self.screen.blit(self.rocket_image, self.rocket_rect)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = RocketGame()
    game.run()
