import pygame
import pygame.sprite
import spritesheet
import spriteanimate

# unused atm, was gonna use this file to hold all the images for
# pacman, ghosts, fruits, bricks, pellets, and powerpellets


class Images(pygame.sprite.Sprite):
    def __init__(self, screen, settings):

        pac_ss = spritesheet.SpriteSheet('/images/pacman.png')
        # pac_imgs = []
        # pac_imgs = [pac_ss.images_at((0, 0, 32, 32), (33, 0, 32, 32), (65, 0, 32, 32), (97, 0, 32, 32),
                                    # (129, 0, 32, 32), (161, 0, 32, 32), (193, 0, 32, 32), (225, 0, 32, 32),
                                    # (257, 0, 32, 32), (389, 0, 32, 32), (321, 0, 32, 32), (353, 0, 32, 32),
                                    # (0, 33, 32, 32), (33, 33, 32, 32), (65, 33, 32, 32), (97, 33, 32, 32),
                                    # (129, 33, 32, 32), (161, 33, 32, 32), (193, 33, 32, 32), (225, 33, 32, 32),
                                    # (257, 33, 32, 32), (389, 33, 32, 32), (321, 33, 32, 32), (353, 33, 32, 32),
                                    # colorkey=(255, 255, 255))]

        self.pac_left = [pac_ss.images_at(((0, 33, 32, 32), (33, 33, 32, 32), (65, 33, 32, 32),
                                      (97, 33, 32, 32), (129, 33, 32, 32), (161, 33, 32, 32),
                                      (193, 33, 32, 32), (225, 33, 32, 32), (257, 33, 32, 32)))]
        self.pac_down = [pac_ss.images_at(((0, 0, 32, 32), (33, 0, 32, 32), (65, 0, 32, 32),
                                      (97, 0, 32, 32), (129, 0, 32, 32), (161, 0, 32, 32),
                                      (193, 0, 32, 32), (225, 0, 32, 32), (257, 0, 32, 32)))]
        self.pac_right = [pygame.transform.flip(self.pac_left, True, False)]
        self.pac_up = [pygame.transform.flip(self.pac_down, False, True)]



        ghost_ss = spritesheet.SpriteSheet('/images/ghosts.png')
        blinky = [ghost_ss.images_at(((0, 0, 32, 32), (0, 0, 32, 32)))]
        pinky = []
        inky = []
        clyde = []





