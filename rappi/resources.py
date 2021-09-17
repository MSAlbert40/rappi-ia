import pygame as py


# Logo of Game
class Logos:
    def __init__(self):
        self.rappi = py.image.load('assets/images/logo.png')


# Background of Game
class Backgrounds:
    def __init__(self, w, h):
        self.dashboard = py.image.load('assets/images/dashboard.png')
        self.dashboard = py.transform.scale(self.dashboard, (w, h))