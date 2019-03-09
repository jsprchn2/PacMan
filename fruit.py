from brick import Bricks
from random import choice


class Fruit(Bricks):
    """Inherits from maze.Block to represent a fruit available for pickup in the maze"""
    def __init__(self, x, y, width, height):
        images = ['apple.png', 'cherry.png', 'orange.png', 'strawberry.png']
        # fruit_image, _ = ImageManager(img=choice(images), resize=(width // 2, height // 2)).get_image()
        # super(Fruit, self).__init__(x, y, width, height, fruit_image)
