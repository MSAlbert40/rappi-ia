import csv
import numpy as np
import random as rd
from os import path

from rappi.resources import *


# Map of Game
class GameMap(Buildings, Colors):
    def __init__(self, w, h):
        Colors.__init__(self)
        self.dimensions = 25
        self.width = w // self.dimensions
        self.height = h // self.dimensions
        Buildings.__init__(self, self.dimensions, self.dimensions)
        with open(path.join('assets', 'maps', f'map.csv'), 'r') as csvFile:
            reader = csv.reader(csvFile)
            self.map = [[0 for c in range(self.height)] for r in range(self.width)]
            for i, row in enumerate(reader):
                for j, gridValue in enumerate(row):
                    psx = i * self.dimensions
                    psy = j * self.dimensions
                    self.map[i][j] = (int(gridValue), py.Rect(psx, psy, self.dimensions, self.dimensions))
        csvFile.close()

    def posBuilding(self):
        demo = [[0 for c in range(self.height)] for r in range(self.width)]
        for c in range(self.width):
            for r in range(self.height):
                demo[c][r] = self.map[c][r]

        # Choose Building Position
        for c in range(self.width):
            for r in range(self.height):
                choose = rd.randint(2, 8)
                value, rect = demo[c][r]
                if value == 2:
                    self.map[c][r] = (choose, rect)

        # Put Traffic-Lights in Map
        count = 0
        while count < 25:
            rx = rd.randint(0, self.width - 1)
            ry = rd.randint(0, self.height - 1)
            value, rect = demo[rx][ry]
            if value == 1:
                access = rd.randint(0, 1)
                if access == 1:
                    self.map[rx][ry] = (9, rect)
                    count = count + 1
                else:
                    self.map[rx][ry] = (10, rect)
                    count = count + 1

        # Start Position
        # rx = rd.randint(0, self.width - 1)
        # ry = rd.randint(0, self.height - 1)
        # value, rect = demo[rx][ry]
        # if value == 0:
            # self.map[rx][ry] = (-1, rect)

    def getRects(self):
        rects = [[0 for c in range(self.height)] for r in range(self.width)]
        for c in range(self.width):
            for r in range(self.height):
                _, rects[c][r] = self.map[c][r]

        news = []
        for c in range(self.width):
            for r in range(self.height):
                news.append(rects[c][r])
        return news

    def getPosition(self, collide):
        nRows, nColumns = self.width, self.height
        psx = collide % nColumns
        psy = collide // nColumns
        return psx, psy

    def getMatrix(self):
        matrix = [[0 for c in range(self.height)] for r in range(self.width)]
        for c in range(self.width):
            for r in range(self.height):
                matrix[c][r], _ = self.map[c][r]
        return matrix

    def drawMap(self, surface):
        for c in range(self.width):
            for r in range(self.height):
                value, rect = self.map[c][r]
                if value == 1:
                    py.draw.rect(surface, self.dark, rect)
                elif value == 2:
                    surface.blit(self.first, (c * self.dimensions, r * self.dimensions))
                elif value == 3:
                    surface.blit(self.second, (c * self.dimensions, r * self.dimensions))
                elif value == 4:
                    surface.blit(self.third, (c * self.dimensions, r * self.dimensions))
                elif value == 5:
                    surface.blit(self.fourth, (c * self.dimensions, r * self.dimensions))
                elif value == 6:
                    surface.blit(self.fifth, (c * self.dimensions, r * self.dimensions))
                elif value == 7:
                    surface.blit(self.sixth, (c * self.dimensions, r * self.dimensions))
                elif value == 8:
                    surface.blit(self.seventh, (c * self.dimensions, r * self.dimensions))
                elif value == 9:
                    # py.draw.rect(surface, self.grass, rect)
                    surface.blit(self.green, (c * self.dimensions, r * self.dimensions))
                elif value == 10:
                    # py.draw.rect(surface, self.blood, rect)
                    surface.blit(self.red, (c * self.dimensions, r * self.dimensions))
                elif value == 11:
                    py.draw.rect(surface, self.skyblue, rect)