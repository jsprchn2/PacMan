import pygame
from pygame.locals import *
from pacma2n import PacMan
from brick import Brick

def axis_overlap(p1, length1, p2, length2):
    collided = False
    if p1 < p2:
        if p2+length2-p1 < length1+length2:
            collided = True
    elif p1 > p2:
        if p1+length1-p2 < length1+length2:
            collided = True
    elif p1 == p2:
        collided = True
    return collided

pygame.init()
width, height = (50,50)
SCREEN_SIZE = (1200, 800)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
x,y = (500,200)
x2,y2,width2,height2 = (150,150,150,100)
background = pygame.surface.Surface(SCREEN_SIZE).convert()
background.fill((0,0,0))
pacman = PacMan((50,50), [500,200])
brick = Brick((150,150), [150,100])
direction = 'LEFT'

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pacman.move()
    pacman.collide(brick)
    screen.blit(background, (0,0))
    brick.draw(screen)
    pacman.draw(screen)
    pygame.display.update()