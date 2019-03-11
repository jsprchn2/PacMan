import pygame
import pygame.font

WHITE = (255, 255, 255)


class GameStats():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.height = 50
        self.width = 50
        img = pygame.image.load('images/frames/pacmanH.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.rect.x, self.rect.y = 310, 515
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.pacmanimage = img
        self.rect = self.pacmanimage.get_rect()
        self.pacpos = ((self.settings.screen_width / 2) + 250, (self.settings.screen_height / 8) - 25)
        self.pacpos2 = ((self.settings.screen_width / 2) + 300, (self.settings.screen_height / 8) - 25)
        self.pacpos3 = ((self.settings.screen_width / 2) + 350, (self.settings.screen_height / 8) - 25)

        # Lives display text
        self.text_color = (30, 30, 30)
        font = pygame.font.Font(None, 72)
        self.font = pygame.font.SysFont(None, 48)
        self.Livestext = font.render("LIVES ", 2, WHITE)
        self.Livespos = self.Livestext.get_rect()
        self.Livespos = ((self.settings.screen_width / 2) + 250, (self.settings.screen_height / 8) - 75)

        # Score display text
        self.text_color = (30, 30, 30)
        font = pygame.font.Font(None, 72)
        self.font = pygame.font.SysFont(None, 48)
        self.scores = font.render("SCORE ", 2, WHITE)
        self.scorespos = self.scores.get_rect()
        self.scorespos = ((self.settings.screen_width / 2) + 225, (self.settings.screen_height / 8) + 100)

    def blitstats(self):
        self.screen.blit(self.Livestext, self.Livespos)
        self.screen.blit(self.pacmanimage, self.pacpos)
        self.screen.blit(self.pacmanimage, self.pacpos2)
        self.screen.blit(self.pacmanimage, self.pacpos3)
        self.screen.blit(self.scores, self.scorespos)

