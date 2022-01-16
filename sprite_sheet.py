import pg_init
import pygame

class SpriteSheet:
    def __init__(self, filepath ):
        self.sheet = pygame.image.load(filepath).convert()

#Load specific sprite from a specific loaction (rectangle)
def spriteLocation(self, rectangle):

    rectangle = pygame.Rect(rectangle)
    sprite = pygame.surface(rectangle.size).convert()
    sprite.blit(self.sheet, (0,0), rectangle)
    return sprite

def loadAllSprites(self):
    sprites = []
    size = 106
    for x in range(4):
        for y in range(2):
            sprites.append(spriteLocation(( x*size,y*size,size+size*x,size+size*y )))
    return sprites

ss = SpriteSheet('Sprite Sheets\index.png')
ss.loadAllSprites()
