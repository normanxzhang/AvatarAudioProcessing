import pygame as pg
from pygame.locals import *


pg.init()
# Global variables for easy changes
screen_width = 600
screen_height = 450
timer = None
window = None
fps = 30


bg = pg.Color('#ABDEE6')
timer = pg.time.Clock()
window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("HackED")
mouse_click = False



class button():
    def __init__(self, color, x,y,width,height, elevation, text=''):
        self.elevation = elevation
        self.dyn_elevation = elevation
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),border_radius=25)

        pg.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),border_radius=25)


        if self.text != '':
            font = pg.font.SysFont('cambria', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def over(self,pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


def draw_window():
    window.fill(bg)
    char_1.draw(window,(0,0,0))


char_1 = button('#FFC8A2', screen_width/2 - 125, screen_height/2 - 50, 250, 100,6,'Start')

# Game loop
run = True
while run == True:
    draw_window()
    pg.display.update()

    # Check input
    for event in pg.event.get():
        pos = pg.mouse.get_pos()

        if (event.type == QUIT):
            run = False

        if pg.mouse.get_pressed()[0]:
            if char_1.over(pos):
                mouse_click = True
        else:
            if mouse_click == True:
                print('click')
                mouse_click = False

        if event.type == pg.MOUSEMOTION:
            if char_1.over(pos):
                char_1.color = ('#FFC8A2')
  
            else:
                char_1.color = ('#FFC8A2')

        # Update screen
        pg.display.update()
        timer.tick(fps)

