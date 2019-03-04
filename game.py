import pygame

import game_functions as gf

from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings


def run_game():
    # setup pygame, settings, and display
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('Pacman Portal')
    clock = pygame.time.Clock()

    # setup game stats and scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    blocks = Group()
    powerpills = Group()
    shield = Group()
    portal = Group()



    while True:
        clock.tick(70)  # 70 fps
        if not stats.game_active:
            quit_game = not gf.startup_screen(ai_settings, stats, screen)
            if quit_game:
                pygame.quit()
                break

        if stats.game_active:



run_game()
