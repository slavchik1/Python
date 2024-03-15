import sys
import pygame
from settings import Settings
from ship import Ship


class Game:
    def __int__(self):
        self.ship = Ship()

    def run_game(self):
        pygame.init()
        settings = Settings()
        pygame.display.set_mode((1200, 800))
        pygame.display.set_caption(settings.window_name)
        pygame.display.set_icon(pygame.image.load("images/icon.jpeg"))
        self.ship.bitme()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()



if __name__ == "__main__":
    game = Game()
    game.run_game()
