import pygame

class spritesheet:
    def __init__(self, filepath ):
        self.sheet = pygame.image.load(filepath).convert()

#Load sprites from a specific loaction

def imageLoc(self, shape, colour = None):

    shape = pygame.Shape(shape)
    sprite = pygame.surface(shape.size).convert()
    sprite.blit(self.sheet, (0,0), shape)
    if colour is not None:
        if colour is -1:
            colour = sprite.getLoc(0,0)



def imagesLoc(self,shapes, colour = None):
    return[self.imageLoc(shape,)]
