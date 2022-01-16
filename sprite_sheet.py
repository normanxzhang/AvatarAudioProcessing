import pygame

class SpriteSheet:
    def __init__(self, filepath ):
        self.sheet = pygame.image.load(filepath).convert()

    #Load specific sprite from a specific loaction (rectangle)
    def spriteLocation(self, rectangle):

        rectangle = pygame.Rect(rectangle)
        sprite = pygame.Surface(rectangle.size).convert()
        sprite.blit(self.sheet, (0,0), rectangle)
        return sprite

    def loadAllSprites(self):
        sprites = []
        size = 105
        for y in range(2):
            for x in range(4):
                sprites.append(self.spriteLocation((x*size, y*size, size, size)))
        return sprites


