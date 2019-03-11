import pygame
from pygame.sprite import Sprite


class Bricks(Sprite):
    def __init__(self, screen):
        super(Bricks, self).__init__()
        self.screen = screen
        self.height = 10
        self.width = 10
        img = pygame.image.load('images/brick.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

    def blitbricks(self):
        self.screen.blit(self.image, self.rect)
