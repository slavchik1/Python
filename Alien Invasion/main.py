import sys
import pygame
from settings import Settings


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.window_width, settings.window_height))
    pygame.display.set_caption(settings.window_name)
    pygame.display.set_icon(pygame.image.load("images/icon.jpeg"))

run_game()

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
