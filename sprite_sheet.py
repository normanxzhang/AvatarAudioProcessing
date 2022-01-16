import pygame

class SpriteSheet:
    def __init__(self, filepath,scaling):
        self.sheet = pygame.image.load(filepath).convert_alpha()
        self.sheet = pygame.transform.scale(self.sheet,scaling)

    #Load specific sprite from a specific loaction (rectangle)
    def spriteLocation(self, rectangle,colour):

        rectangle = pygame.Rect(rectangle)
        sprite = pygame.Surface(rectangle.size).convert_alpha()
        #sprite  = pygame.transform.scale(sprite, (200, 200))
        sprite.fill(colour)
        sprite.blit(self.sheet, (0,0), rectangle)
        return sprite

    def loadRow(self, rowNumber):
        sprites = []
        size = 400
        if rowNumber <= 4:
            colour = '#FF0000'
        elif rowNumber <= 9:
            colour = '#FFA500'
        elif rowNumber <= 14:
            colour = '#00FF00'
        elif rowNumber <= 19:
            colour = '#7F00FF'

        for x in range(10):
            sprites.append(self.spriteLocation((x*size, rowNumber*size, size, size),colour))
        return sprites

    def slime_preview(self,row):
        size = 200
        return self.spriteLocation((0,row*size,size,size),'#E8DFF5')
