import pygame as pg
from pygame.locals import *
import sprite_sheet
import animation as ani

pg.init()
# Global variables for easy changes
screen_width = 600
screen_height = 450
window = None
fps = 30
bg = pg.Color(0,255,0)
window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("HackED")
mouse_click = False

#array of Animation objects
animations = []

def loadAnimations():
    ss = sprite_sheet.SpriteSheet('Sprite Sheets\index.png')
    spritesRow1 = ss.loadRow(1)
    spritesRow2 = ss.loadRow(2)

    animations.append(ani.Animation("Idle", spritesRow1, 10))
    animations.append(ani.Animation("Talking", spritesRow2, 20))

def playAni(number): 
    
    animations[number].playAnimation(window)
        

class button():
    def __init__(self, color, x,y,width,height, text=''):

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
    start_btn.draw(window,(0,0,0))


start_btn = button('#ABDEE6', screen_width/2 - 125, screen_height/2 + 100, 250, 100,'Start')
delay = 0
# Game loop
run = True
flag = False
loadAnimations()
while run == True:
    if not flag:
        draw_window()
    else:
        window.fill(bg)
    #pg.display.update()
    playAni(0)
    # Check input
    for event in pg.event.get():
        pos = pg.mouse.get_pos()

        if (event.type == QUIT):
            run = False

        if not flag:
            if pg.mouse.get_pressed()[0]:
                if start_btn.over(pos):
                    mouse_click = True
                    start_btn = button('#ABDEE6', screen_width/2 - 125, screen_height/2 + 105, 250, 100,'Start')
            else:
                if mouse_click == True:
                    print('click')
                    mouse_click = False
                    flag = True

        if event.type == pg.MOUSEMOTION:
            if start_btn.over(pos):
                start_btn.color = ('#ABDEE6')
  
            else:
                start_btn.color = ('#ABDEE6')

    # Update screen
    pg.display.update()
