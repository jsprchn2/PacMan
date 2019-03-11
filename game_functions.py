import pygame
from pygame.sprite import Group
import sys
from brick import Bricks
from shield import Shield
from powerpellets import PowerPellets, Pellets
from portal import Portal


def check_events(pacman):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, pacman)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pacman)


def check_keydown_events(event, pacman):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        pacman.moving_up = True
    elif event.key == pygame.K_DOWN:
        pacman.moving_down = True
    elif event.key == pygame.K_RIGHT:
        pacman.moving_right = True
    elif event.key == pygame.K_LEFT:
        pacman.moving_left = True
    elif event.key == pygame.K_SPACE:
        pass
    elif event.key == pygame.QUIT:
        sys.exit()


def check_keyup_events(event, pacman):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        pacman.moving_right = False
    elif event.key == pygame.K_LEFT:
        pacman.moving_left = False
    elif event.key == pygame.K_UP:
        pacman.moving_up = False
    elif event.key == pygame.K_DOWN:
        pacman.moving_down = False


# Check direction pacman is going to compare and see if he can't go a direction anymore if he hit a block
def check_direction(pacman, block):
    left = False
    right = False
    up = False
    down = False
    if pacman.rect.centerx <= block.rect.centerx:
        right = True
    else:
        left = True
    if pacman.rect.y + pacman.rect.height / 2 <= block.rect.y + block.rect.height / 2:
        up = True
    else:
        down = True

    if left:
        pacman.x += 1
    elif right:
        pacman.x -= 1
    if up:
        pacman.y -= 1
    elif down:
        pacman.y += 1


# Check the direction pacman is going for the collision with the shield
def check_shield_direction(pacman, shield):
    left = False
    right = False
    up = False
    down = False

    if pacman.rect.centerx <= shield.rect.centerx:
        right = True
    else:
        left = True
    if pacman.rect.y + pacman.rect.height / 2 <= shield.rect.y + shield.rect.height / 2:
        up = True
    else:
        down = True

    if left:
        pacman.x += 1
    elif right:
        pacman.x -= 1
    if up:
        pacman.y -= 1
    elif down:
        pacman.y += 1


# Pacman collision handling
def check_collision(pacman, blocks, pellets, powerpellets, shield, fruits):
    for block in blocks:
        if pygame.sprite.collide_rect(pacman, block):
            print("collided")
            check_direction(pacman, block)
    for theshield in shield:
        if pygame.sprite.collide_rect(pacman, theshield):
            print("shield")
            check_shield_direction(pacman, theshield)
    for powerpellet in powerpellets:
        if pygame.sprite.collide_rect(pacman, powerpellet):
            print("Eaten")
            powerpellet.remove(powerpellets)
    for pellet in pellets:
        if pygame.sprite.collide_rect(pacman, pellet):
            print("Eaten")
            pellet.remove(pellets)
    for fruit in fruits:
        if pygame.sprite.collide_rect(pacman, fruits):
            print("Eaten")
            fruit.remove(fruits)


# Read in text file of maze and then fill in X's with a block
def readFile(screen, blocks, shield, pellets, powerpellets):
    file = open("maze.txt", "r")
    contents = file.read()
    line = ''
    all_lines = []
    for chars in contents:
        if chars != '\n':
            line += chars
        else:
            all_lines.append(line)
            line = ''
    i = 0
    j = 0
    for rows in all_lines:
        for chars in rows:
            if chars == 'X':
                new = Bricks(screen)
                new.rect.x, new.rect.y = 13 * i, 13 * j
                blocks.add(new)
            elif chars == 'P':
                thepowerpellets = PowerPellets(screen)
                thepowerpellets.rect.x, thepowerpellets.rect.y = 13 * i, 13 * j
                powerpellets.add(thepowerpellets)
            elif chars == '-':
                theshield = Shield(screen)
                theshield.rect.x, theshield.rect.y = 13 * i, 13 * j
                shield.add(theshield)
            elif chars == 'o':
                thepellets = Pellets(screen)
                thepellets.rect.x, thepellets.rect.y = 13 * i, 13 * j
                pellets.add(thepellets)
            elif chars == 'T':
                pass
            i += 1
        i = 0
        j += 1
