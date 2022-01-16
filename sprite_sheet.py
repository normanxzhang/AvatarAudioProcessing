import pygame

class SpriteSheet:
    def __init__(self, filepath ):
        self.sheet = pygame.image.load(filepath).convert_alpha()

    #Load specific sprite from a specific loaction (rectangle)
    def spriteLocation(self, rectangle):

        rectangle = pygame.Rect(rectangle)
        sprite = pygame.Surface(rectangle.size).convert_alpha()
        sprite  = pygame.transform.scale(sprite, (200, 200))
        sprite.fill((0, 255, 255))
        sprite.blit(self.sheet, (0,0), rectangle)
        return sprite

    def loadRow(self, rowNumber):
        sprites = []
        size = 106
        for y in range(rowNumber):
            for x in range(4):
                sprites.append(self.spriteLocation((x*size, y*size, size, size)))
        return sprites

