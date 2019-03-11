import pygame
import spritesheet
import spriteanimate
import images


class Pacman():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.height = 35
        self.width = 35
        self.lives = 3

        # check with single frames first
        img = pygame.image.load('images/frames/pacmanH.png')
        # self.p_left = img
        # self.p_right = pygame.transform.flip(img, True, False)
        # self.p_up = pygame.transform.rotate(img, -90)
        # self.p_down = pygame.transform.rotate(img, 90)

        self.pac_left = [pygame.image.load('images/frames/pacmanH.png'),
                         pygame.image.load('images/frames/pacmanH2.png'),
                         pygame.image.load('images/frames/pacmanH4.png')]
        self.pac_down = [pygame.image.load('images/frames/pacmanV.png'),
                         pygame.image.load('images/frames/pacmanV2.png'),
                         pygame.image.load('images/frames/pacmanV4.png')]
        self.pac_right = [pygame.transform.flip(self.pac_left[0], True, False),
                          pygame.transform.flip(self.pac_left[1], True, False),
                          pygame.transform.flip(self.pac_left[2], True, False)]
        self.pac_up = [pygame.transform.flip(self.pac_down[0], False, True),
                       pygame.transform.flip(self.pac_down[1], False, True),
                       pygame.transform.flip(self.pac_down[2], False, True)]
        self.death = [pygame.image.load('images/frames/pacmanHD1.png'),
                      pygame.image.load('images/frames/pacmanHD2.png'),
                      pygame.image.load('images/frames/pacmanHD3.png'),
                      pygame.image.load('images/frames/pacmanVD1.png'),
                      pygame.image.load('images/frames/pacmanVD2.png'),
                      pygame.image.load('images/frames/pacmanVD3.png')
                      ]
        self.image = img
        self.image_index = 0
        self.death_index = 0
        self.frames = 3
        self.direction = "Left"

        # attempts at making sprite sheet or using subsurface to cut up spritesheet image
        # pac_ss = pygame.image.load('images/pacman.png').convert_alpha()
        # pac_imgs = (self.pac_down, self.pac_left)
        # for y, img_list in enumerate(pac_imgs):
        #     for x in range(12):
        #         img_list.append(pac_ss.subsurface(x * 32, y * 32, 32, 32))
        #
        # for pl in self.pac_left:
        #     self.pac_right.append(self.pac_left[pl])
        # pac_ss = spritesheet.SpriteSheet('images/pacman.png')
        # self.pac_down = [pac_ss.images_at(((0, 33, 32, 32), (33, 33, 32, 32), (65, 33, 32, 32),
        #                                    (97, 33, 32, 32), (129, 33, 32, 32), (161, 33, 32, 32),
        #                                    (193, 33, 32, 32), (225, 33, 32, 32), (257, 33, 32, 32)))]
        # self.pac_left = [pac_ss.images_at(((0, 0, 32, 32), (33, 0, 32, 32), (65, 0, 32, 32),
        #                                    (97, 0, 32, 32), (129, 0, 32, 32), (161, 0, 32, 32),
        #                                    (193, 0, 32, 32), (225, 0, 32, 32), (257, 0, 32, 32)))]
        # self.pac_right = []  # [pygame.transform.flip(self.pac_left, True, False)]
        # self.pac_up = []  # [pygame.transform.flip(self.pac_down, False, True)]
        # self.pac_index = 0
        # for pac_index in range(len(self.pac_left)):
        #     self.pac_right.append(pygame.transform.flip(self.pac_left[pac_index], True, False))
        # for pac_index in self.pac_up:
        #     self.pac_right.append(pygame.transform.flip(self.pac_down[pac_index], False, True))
        # self.image = self.image[self.image_index]
        self.rect = img.get_rect()
        self.rect.x, self.rect.y = 310, 515
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

        self.x, self.y = 300, 500
        self.rect.x, self.rect.y = self.x, self.y

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        self.rect.x, self.rect.y = self.x, self.y
        if self.image_index >= self.frames:
            self.image_index = 0
        else:
            if self.moving_right:
                self.x += self.settings.pacspd
                self.direction = "Right"
                self.image = self.pac_right[self.image_index]
                self.image_index += 1
            elif self.moving_left:
                self.x -= self.settings.pacspd
                self.direction = "Left"
                self.image = self.pac_left[self.image_index]
                self.image_index += 1
            elif self.moving_up:
                self.y -= self.settings.pacspd
                self.direction = "Up"
                self.image = self.pac_up[self.image_index]
                self.image_index += 1
            elif self.moving_down:
                self.y += self.settings.pacspd
                self.direction = "Down"
                self.image = self.pac_down[self.image_index]
                self.image_index += 1

    def blitpacman(self):
        self.screen.blit(self.image, self.rect)



