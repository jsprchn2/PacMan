import pygame
from vector import Vector


UP = Vector(0, -1, 0)
DOWN = Vector(0, 1, 0)
LEFT = Vector(-1, 0, 0)
RIGHT = Vector(1, 0, 0)
STOP = Vector(None, None, None)


class Node():
    def __init__(self, row, column):
        self.row, self.column = row, column
        # self.