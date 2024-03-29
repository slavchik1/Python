import pygame

class Settings:
    def __init__(self):
        self.bg_color = (60, 47, 86)
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_speed = 0.5

        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        pygame.display.set_caption("Alien Invasion")
        pygame.display.set_icon(pygame.image.load("images/icon.jpeg"))
