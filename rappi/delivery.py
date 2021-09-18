from rappi.resources import *


class Direction:
    LEFT, RIGHT, DOWN, UP = range(4)


class Attributes:
    def __init__(self, psx, psy, w, h):
        self.psx, self.psy = psx, psy
        self.w, self.h = w, h


class Delivery(Attributes, Colors, SpriteSheet):
    def __init__(self, psx, psy, w, h, image, sprite=None, direction=Direction.RIGHT, frame=0):
        Attributes.__init__(self, psx, psy, w, h)
        SpriteSheet.__init__(self)
        Colors.__init__(self)
        self.image = image
        self.frameIndex = 0
        self.direction = direction
        self.frame = frame
        self.sprite = sprite
        if self.sprite is not None:
            frames = []
            for i in range(15):
                frames.append((i * 25, 0, 25, 25))

            self.images = [None] * 4
            for position in [Direction.LEFT, Direction.RIGHT, Direction.DOWN, Direction.UP]:
                a = position * 3
                b = a + 3
                self.images[position] = self.images_at(frames[a:b], self.delivery)

    def move(self):
        if self.direction == Direction.UP:
            self.psy -= self.image
        elif self.direction == Direction.DOWN:
            self.psy += self.image
        elif self.direction == Direction.LEFT:
            self.psx -= self.image
        elif self.direction == Direction.RIGHT:
            self.psx += self.image

        if self.frameIndex < 2:
            self.frameIndex += 1
        else:
            pass

    def stop(self):
        self.frameIndex = 0

    def blit_on(self, screen, debug=False):
        if self.images is not None:
            screen.blit(self.images[self.direction][self.frameIndex], (self.psx, self.psy))
        if debug:
            py.draw.rect(screen, self.cposition, (self.psx, self.psy, 25, 25), 1)