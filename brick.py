import pygame
from pygame.sprite import Sprite


class Blocks(Sprite):
    def __init__(self, screen):
        super(Blocks, self).__init__()
        self.screen = screen
        self.height = 10
        self.width = 10
        img = pygame.image.load('images/square.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

    def blitblocks(self):
        self.screen.blit(self.image, self.rect)