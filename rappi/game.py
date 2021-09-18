import sys
import pygame as py
from os import path
from pygame.locals import *
from rappi.map import *
from rappi.delivery import *
from rappi.resources import *
from algorithms.astar import *


# Size of Screen
WIDTH, HEIGHT = 650, 650

# Time of Execute Screen
mainTime = py.time.Clock()

# Initialize the Game
py.init()

# Initialize Variables
logo = Logos()
areas = Areas()
star = AStar()
background = Backgrounds(WIDTH, HEIGHT)
mapPrincipal = GameMap(areas.areaMap.get_width(), areas.areaMap.get_height())
delivery = Delivery(0, 0, 25, 25, 4, SpriteSheet())

# Create the Screen and Customize tittle
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_icon(logo.rappi)
py.display.set_caption('Rappi Delivery | Algorithm A*')


# Start Game
def startGame():
    mapPrincipal.posBuilding()
    move, current = None, None
    path, pc = [], 1
    while True:
        screen.blit(background.dashboard, (0, 0))
        screen.blit(areas.areaMap, (0, 0))
        # mapPrincipal.drawMap(areas.areaMap)

        for e in py.event.get():
            if e.type == QUIT:
                py.quit()
                sys.exit()
            elif e.type == py.MOUSEBUTTONDOWN and move is None:
                mx, my = py.mouse.get_pos()
                mx, my = int(mx/25)*25, int(my/25)*25

                mouseRect = py.Rect(mx, my, 25, 25)
                mapRects = mapPrincipal.getRects()
                collide = mouseRect.collidelist(mapRects)

                psx, psy = mapPrincipal.getPosition(collide)
                print(psx, psy)
                grid, _ = mapPrincipal.map[psy][psx]
                print(grid)

                if grid == 1:
                    _, pr = mapPrincipal.map[psy][psx]
                    mapPrincipal.map[psy][psx] = (11, pr)
                    if current is not None:
                        pa, pb = current
                        _, pd = mapPrincipal.map[pa][pb]
                        mapPrincipal.map[pa][pb] = (1, pd)
                    current = (psy, psx)

                    mapping = mapPrincipal.getMatrix()
                    startDelivery = (delivery.psx // 25, delivery.psy // 25)
                    pp, examined = star.solveAStar(mapping, startDelivery, (psx, psy), Node.Manhattan)
                    numberPath = len(pp)
                    print(examined)
                    for i in range(numberPath - 1):
                        psy1, psx1 = pp[i]
                        psy2, psx2 = pp[i + 1]
                        difx, dify = psx2 - psx1, psy2 - psy1
                        if difx > 0:
                            path.append(Direction.RIGHT)
                        elif difx < 0:
                            path.append(Direction.LEFT)
                        elif dify > 0:
                            path.append(Direction.DOWN)
                        elif dify < 0:
                            path.append(Direction.UP)

        areas.areaMap.fill((48, 51, 49))
        mapPrincipal.drawMap(areas.areaMap)
        delivery.blit_on(areas.areaMap)
        if pc == 9:
            if len(path) > 0:
                move = path.pop(0)
            else:
                move = None
            pc = 1
        if move is not None:
            delivery.direction = move
            delivery.move()
        pc += 1
        mainTime.tick(60)
        py.display.update()