import pygame
from pygame.sprite import Group


class Ghosts():
    def __init__(self, screen, color):
        super(Ghosts, self).__init__()
        i = 0
        self.screen = screen
        self.height = 32
        self.width = 32

        ss_ghost = pygame.image.load('images/ghosts.png')


        img = ''
        if color == "red":
            img = pygame.image.load('images/frames/redD1.png')
        elif color == "cyan":
            img = pygame.image.load('images/frames/pinkL1.png')
            i = 30
        elif color == "orange":
            img = pygame.image.load('images/frames/blueR1.png')
            i = 85
        elif color == "pink":
            img = pygame.image.load('images/frames/orangeU1.png')
            i = 52

        image = pygame.transform.scale(img, (self.height, self.width))
        self.rect = image.get_rect()
        self.rect.x, self.rect.y = 275 + i, 315
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.image = image

        self.ghost_up = False
        self.ghost_down = False
        self.ghost_left = False
        self.ghost_right = False

    def update(self):
        if self.ghost_left:
            self.rect.x -= 1
        elif self.ghost_right:
            self.rect.x += 1
        elif self.ghost_up:
            self.rect.y -= 1
        elif self.ghost_down:
            self.rect.y += 1

    def blitghosts(self):
        self.screen.blit(self.image, self.rect)
