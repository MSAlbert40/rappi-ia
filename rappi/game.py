import sys
import pygame as py
from pygame.locals import *
from rappi.resources import *

# Size of Screen
WIDTH, HEIGHT = 1300, 650

# Time of Execute Screen
mainTime = py.time.Clock()

# Initialize the Game
py.init()

# Initialize Variables
logo = Logos()
background = Backgrounds(WIDTH, HEIGHT)

# Create the Screen and Customize tittle
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_icon(logo.rappi)
py.display.set_caption('Rappi Delivery | Algorithm A*')


# Start Game
def startGame():
    while True:
        screen.blit(background.dashboard, (0, 0))
        for e in py.event.get():
            if e.type == QUIT:
                py.quit()
                sys.exit()
        mainTime.tick(60)
        py.display.update()