import pygame

class SpriteSheet:
    def __init__(self, filepath):
        self.sheet = pygame.image.load(filepath).convert_alpha()
        self.sheet = pygame.transform.scale(self.sheet,(4000,8000))

    #Load specific sprite from a specific loaction (rectangle)
    def spriteLocation(self, rectangle):

        rectangle = pygame.Rect(rectangle)
        sprite = pygame.Surface(rectangle.size).convert_alpha()
        #sprite  = pygame.transform.scale(sprite, (200, 200))
        sprite.fill('#FFFFFF')
        sprite.blit(self.sheet, (0,0), rectangle)
        return sprite

    def loadRow(self, rowNumber):
        sprites = []
        size = 400
        for y in range(rowNumber):
            for x in range(10):
                sprites.append(self.spriteLocation((x*size, y*size, size, size)))
        return sprites
