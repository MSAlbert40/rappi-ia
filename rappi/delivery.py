from rappi.resources import *


class Direction:
    LEFT, RIGHT, DOWN, UP = range(4)


class Attributes:
    def __init__(self, psx, psy, w, h):
        self.psx, self.psy = psx, psy
        self.w, self.h = w, h


class Delivery(Attributes, Colors, SpriteSheet):
    def __init__(self, psx, psy, w, h, vel, sprite=None, direction=Direction.RIGHT, frame=0):
        super().__init__(psx, psy, w, h)
        SpriteSheet.__init__(self)
        Colors.__init__(self)
        self.vel = vel
        self.direction = direction
        self.frame = frame
        self.sprite = sprite

        if self.sprite is not None:
            frames = []
            for i in range(15):
                frames.append((i * 32, 0, 32, 32))

            self.images = [None] * 4
            for position in [Direction.LEFT, Direction.RIGHT, Direction.DOWN, Direction.UP]:
                a = position * 3
                b = a + 3
                self.images[position] = self.sprite.images_at(frames[a:b], self.delivery)

    def move(self):
        if self.direction == Direction.UP:
            self.psy -= self.vel
        elif self.direction == Direction.DOWN:
            self.psy += self.vel
        elif self.direction == Direction.LEFT:
            self.psx -= self.vel
        elif self.direction == Direction.RIGHT:
            self.psx += self.vel

        if self.frame < 2:
            self.frame += 1
        else:
            pass

    def stop(self):
        self.frame = 0

    def blit_on(self, screen):
        if self.images is not None:
            screen.blit(self.images[self.direction][self.frame], (self.psx, self.psy))