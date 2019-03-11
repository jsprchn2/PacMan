import pygame
import game_functions as gf
from pacman import Pacman
from Menu import StartScreen
from pygame.sprite import Group
from ghosts import Ghosts
from settings import Settings
from game_stats import GameStats

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)


def __str__(self):
    return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'


def Game():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Pacman Portal")

    startScreen = StartScreen(screen, settings)
    showgamestats = GameStats(screen, settings)

    bricks = Group()
    powerpellets = Group()
    pellets = Group()
    shield = Group()
    fruits = Group()
    portal = Group()

    thepacman = Pacman(screen, settings)

    blinky = Ghosts(screen, "red")
    inky = Ghosts(screen, "cyan")
    clyde = Ghosts(screen, "orange")
    pinky = Ghosts(screen, "pink")

    startScreen.makeScreen(screen)
    gf.readFile(screen, bricks, shield, pellets, powerpellets)

    screen.fill(BLACK)
    while True:
        screen.fill(BLACK)
        showgamestats.blitstats()
        gf.check_events(thepacman)
        gf.check_collision(thepacman, bricks, pellets, powerpellets, shield, fruits)
        thepacman.update()
        for brick in bricks:
            brick.blitbricks()
        for theshield in shield:
            theshield.blitshield()
        for power in powerpellets:
            power.blitpowerpills()
        for pellet in pellets:
            pellet.blitpellet()
        thepacman.blitpacman()
        blinky.blitghosts()
        inky.blitghosts()
        clyde.blitghosts()
        pinky.blitghosts()

        pygame.display.flip()


Game()

