import sys
import pygame as py
from pygame.locals import *
from rappi.map import *
from rappi.resources import *


# Size of Screen
WIDTH, HEIGHT = 1300, 650

# Time of Execute Screen
mainTime = py.time.Clock()

# Initialize the Game
py.init()

# Initialize Variables
logo = Logos()
areas = Areas()
background = Backgrounds(WIDTH, HEIGHT)
mapPrincipal = GameMap(areas.areaMap.get_width(), areas.areaMap.get_height())

# Create the Screen and Customize tittle
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_icon(logo.rappi)
py.display.set_caption('Rappi Delivery | Algorithm A*')


# Start Game
def startGame():
    mapPrincipal.posBuilding()
    while True:
        screen.blit(background.dashboard, (0, 0))
        screen.blit(areas.areaMap, (0, 0))
        mapPrincipal.drawMap(areas.areaMap)

        for e in py.event.get():
            if e.type == QUIT:
                py.quit()
                sys.exit()
        mainTime.tick(60)
        py.display.update()