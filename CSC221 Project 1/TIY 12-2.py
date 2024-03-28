import pygame
from pygame.locals import *

class Dva:
    def __init__(self, screen_width, screen_height, char_image):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.character_image = pygame.image.load(char_image).convert()
        self.character_rect = self.character_image.get_rect()
        self.character_rect.center = (screen_width // 2, screen_height // 2)

    def draw_character(self):
        self.screen.fill((255, 255, 255))  # Set background color to white
        self.screen.blit(self.character_image, self.character_rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.draw_character()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

# bitmap image of D.Va 
character_image_path = "dva.bmp"

# Set your screen dimensions
screen_width = 800
screen_height = 600

# Create an instance of CharacterDrawer and run it
Dva = Dva(screen_width, screen_height, character_image_path)
Dva.run()
