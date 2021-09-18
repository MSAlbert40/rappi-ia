import pygame as py


# Colors of Game
class Colors:
    def __init__(self):
        self.dark = 27, 27, 27
        self.grass = 151, 218, 123
        self.skyblue = 7, 218, 230
        self.blood = 174, 0, 2
        self.transparent = 0, 0, 0, 50


# Logo of Game
class Logos:
    def __init__(self):
        self.rappi = py.image.load('assets/images/logo.png')


# Background of Game
class Backgrounds:
    def __init__(self, w, h):
        self.dashboard = py.image.load('assets/images/dashboard.png')
        self.dashboard = py.transform.scale(self.dashboard, (w, h))


# New Areas Graphics
class Areas(Colors):
    def __init__(self):
        Colors.__init__(self)

        self.areaMap = py.Surface((1300, 550), py.SRCALPHA)
        self.areaMap.fill(self.dark)


# Building's of Game
class Buildings:
    def __init__(self, w, h):
        self.first = py.image.load('assets/images/buildings/building_first.png')
        self.first = py.transform.scale(self.first, (w, h))

        self.second = py.image.load('assets/images/buildings/building_second.png')
        self.second = py.transform.scale(self.second, (w, h))

        self.third = py.image.load('assets/images/buildings/building_third.png')
        self.third = py.transform.scale(self.third, (w, h))

        self.fourth = py.image.load('assets/images/buildings/building_fourth.png')
        self.fourth = py.transform.scale(self.fourth, (w, h))

        self.fifth = py.image.load('assets/images/buildings/building_fifth.png')
        self.fifth = py.transform.scale(self.fifth, (w, h))

        self.sixth = py.image.load('assets/images/buildings/building_sixth.png')
        self.sixth = py.transform.scale(self.sixth, (w, h))

        self.seventh = py.image.load('assets/images/buildings/building_seventh.png')
        self.seventh = py.transform.scale(self.seventh, (w, h))

        self.green = py.image.load('assets/images/traffic-green.png')
        self.green = py.transform.scale(self.green, (w, h))

        self.red = py.image.load('assets/images/traffic-red.png')
        self.red = py.transform.scale(self.red, (w, h))