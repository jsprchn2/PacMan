import pygame
from vector import Vector

WIDTH = 16
HEIGHT = 16
UP = Vector(0, -1, 0)
DOWN = Vector(0, 1, 0)
LEFT = Vector(-1, 0, 0)
RIGHT = Vector(1, 0, 0)
STOP = Vector(None, None, None)
WHITE = (255, 255, 255)


class Node():
    def __init__(self, row, column):
        self.row, self.column = row, column
        self.pos = Vector(column * WIDTH, row * HEIGHT)
        self.neightbors = {UP: None, DOWN: None, LEFT: None, RIGHT: None}

    def render(self, screen):
        for n in self.neightbors.keys():
            if self.neightbors[n] is not None:
                """pygame.draw.line(screen, WHITE, self.pos.toTuple())"""
