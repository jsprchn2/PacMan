import pygame


class Pacman():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.height = 35
        self.width = 35
        self.image = [pygame.image.load('images/pacman1.png'),
                      pygame.image.load('images/pacman2.png')]


        for nrow in range(len(self.rows)):
            row = self.rows[nrow]