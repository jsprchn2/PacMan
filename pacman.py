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
        img = pygame.image.load('images/frames/pacmanH.png')
        self.p_left = img
        self.p_right = pygame.transform.flip(img, True, False)
        self.p_up = pygame.transform.rotate(img, -90)
        self.p_down = pygame.transform.rotate(img, 90)
        self.image = pygame.image.load('images/frames/pacmanH.png')
        self.pac_left = [pygame.image.load('images/frames/pacmanH.png'),
                         pygame.image.load('images/frames/pacmanH2.png'),
                         pygame.image.load('images/frames/pacmanH4.png')]
        self.pac_down = [pygame.image.load('images/frames/pacmanV.png'),
                         pygame.image.load('images/frames/pacmanV2.png'),
                         pygame.image.load('images/frames/pacmanV4.png')]
        self.pac_right = [pygame.transform.flip(self.pac_left[0], True, False),
                          pygame.transform.flip(self.pac_left[1], True, False),
                          pygame.transform.flip(self.pac_left[2], True, False)]
        self.pac_up = [pygame.transform.flip(self.pac_down[0], True, False),
                       pygame.transform.flip(self.pac_down[1], True, False),
                       pygame.transform.flip(self.pac_down[2], True, False)]
        self.death = [pygame.image.load('images/frames/pacmanHD1.png'),
                      pygame.image.load('images/frames/pacmanHD2.png'),
                      pygame.image.load('images/frames/pacmanHD3.png'),
                      pygame.image.load('images/frames/pacmanVD1.png'),
                      pygame.image.load('images/frames/pacmanVD2.png'),
                      pygame.image.load('images/frames/pacmanVD3.png')
                      ]
        self.image_index = 0
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
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 310, 515
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

        self.x, self.y = 300, 500
        self.rect.x, self.rect.y = self.x, self.y
        # For updating pacman and to rotate depending on direction
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    # Updates pacman direction and sprite depending on direction
    def update(self):
        self.rect.x, self.rect.y = self.x, self.y
        if self.moving_right:
            self.x += self.settings.pacspd
            self.direction = "Right"
            self.image = self.p_right
        elif self.moving_left:
            self.x -= self.settings.pacspd
            self.direction = "Left"
            self.image = self.p_left
        elif self.moving_up:
            self.y -= self.settings.pacspd
            self.direction = "Up"
            self.image = self.p_up
        elif self.moving_down:
            self.y += self.settings.pacspd
            self.direction = "Down"
            self.image = self.p_down

    def blitpacman(self):
        self.screen.blit(self.image, self.rect)
        # if pygame.time.get_ticks() % 200 <= 50:
        #     self.screen.blit(self.image[0], self.rect)
        # elif pygame.time.get_ticks() % 200 <= 100:
        #     self.screen.blit(self.image[1], self.rect)
        # elif pygame.time.get_ticks() % 200 <= 150:
        #     self.screen.blit(self.image[2], self.rect)
        # else:
        #     self.screen.blit(self.image[2], self.rect)


