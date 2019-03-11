import pygame
from pygame.sprite import Sprite


class Fruits(Sprite):
    def __init__(self, screen):
        super(Fruits, self).__init__()
        self.screen = screen
        self.height = 5
        self.width = 5
        img = pygame.image.load('images/square.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

    def blitbricks(self):
        self.screen.blit(self.image, self.rect)