import pygame


class Ship:
    def init(self, game):
        self.screen = game.screen()
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("images/SpaceShip.png")
        self.rect = self.image.get_rect()

    def bitme(self):
        self.screen.blit(self.image, self.rect())
