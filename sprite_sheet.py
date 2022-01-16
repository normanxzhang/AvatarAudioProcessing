import pygame

class SpriteSheet:
    def __init__(self, filepath):
        self.sheet = pygame.image.load(filepath).convert_alpha()
        self.sheet = pygame.transform.scale(self.sheet,(800,1800))

    #Load specific sprite from a specific loaction (rectangle)
    def spriteLocation(self, rectangle):

        rectangle = pygame.Rect(rectangle)
        sprite = pygame.Surface(rectangle.size).convert_alpha()
        #sprite  = pygame.transform.scale(sprite, (200, 200))
        sprite.fill((0, 255, 0))
        sprite.blit(self.sheet, (0,0), rectangle)
        return sprite

    def loadRow(self, rowNumber):
        sprites = []
        size = 200
        for y in range(rowNumber):
            for x in range(4):
                sprites.append(self.spriteLocation((x*size, y*size, size, size)))
        return sprites
