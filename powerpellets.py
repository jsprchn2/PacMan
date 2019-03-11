import pygame
from pygame.sprite import Sprite


class PowerPellets(Sprite):
    def __init__(self, screen):
        super(PowerPellets, self).__init__()
        self.screen = screen
        self.height = 14
        self.width = 14
        img = pygame.image.load('images/powerpellet.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

    def blitpowerpills(self):
        self.screen.blit(self.image, self.rect)


class Pellets(Sprite):
    def __init__(self, screen):
        super(Pellets, self).__init__()
        self.screen = screen
        self.height = 7
        self.width = 7
        img = pygame.image.load('images/pellet.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

    def blitpellet(self):
        self.screen.blit(self.image, self.rect)

