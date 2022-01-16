import pygame as pg
clock = pg.time.Clock()
class Animation:

    def __init__(self, name, sprites, delay):
        self.name = name
        self.sprites = sprites
        self.delay = delay
        self.time = 0
        self.currentSprite = 0

    def playAnimation(self, window):
        clock.tick(30)
        if self.time < self.delay:
            self.time += clock.get_time()

        else:
            self.time = 0
            if self.currentSprite < len(self.sprites)-1:
                self.currentSprite += 1
            else:
                self.currentSprite = 0
            # next sprite
        window.blit(self.sprites[self.currentSprite], ( (window.get_width() - self.sprites[self.currentSprite].get_width() )/2, (window.get_height() - self.sprites[self.currentSprite].get_height() )/4))
