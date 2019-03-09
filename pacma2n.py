import pygame
from pygame.sprite import Sprite


class PacMan(Sprite):

    def __init__(self, ai_settings, screen):
        super(PacMan, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('')


    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                self.pos[1] -= 3
                self.direction = 'UP'
            elif event.type == pygame.KEYDOWN:
                self.pos[1] += 3
                self.direction = 'DOWN'
            elif event.type == pygame.K_RIGHT:
                self.pos[0] += 3
                self.direction = 'RIGHT'
            elif event.type == pygame.K_LEFT:
                self.pos[0] -= 3
                self.direction = 'LEFT'

    def collide(self, other):
        xcollide = axis_overlap(self.pos[0], self.dim[0],
                                other.pos[0], other.dim[1])
        ycollide = axis_overlap(self.pos[1], self.dim[1],
                                other.pos[1], other.dim[1])
        if xcollide & ycollide:
            if self.direction is 'UP':
                self.pos[1] = other.pos[1]+other.dim[1]
            elif self.direction is 'DOWN':
                self.pos[1] = other.pos[1]-self.dim[1]
            elif self.direction is 'LEFT':
                self.pos[0] = other.pos[0]+other.dim[0]
            elif self.direction is 'RIGHT':
                self.pos[0] = other.pos[0]-self.dim[0]

    def draw(self, screen):
        values = list(self.pos)+list(self.dim)
        pygame.draw.rect(screen, self.COLOR, values)