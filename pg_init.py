import pygame as pg
from pygame.locals import *
import sprite_sheet
import animation as ani

pg.init()
# Global variables for easy changes
screen_width = 800
screen_height = 600
window = None
fps = 30
bg = pg.Color('#E8DFF5')
window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("HackED")
mouse_click = False

#array of Animation objects
animations = []

def loadAnimations():
    ss = sprite_sheet.SpriteSheet('Sprite Sheets\slime_spritesheet.png',(4000,8000))
    spritesRow1 = ss.loadRow(1)
    spritesRow2 = ss.loadRow(2)

    animations.append(ani.Animation("Idle", spritesRow1, 100))
    animations.append(ani.Animation("Talking", spritesRow2, 100))




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
            font = pg.font.SysFont('cambria', 40)
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
    select_btn1.draw(window,(0,0,0))
    select_btn2.draw(window,(0,0,0))
    select_btn3.draw(window,(0,0,0))
    select_btn4.draw(window,(0,0,0))
    




select_btn1 = button('#ABDEE6', 10, 220, 200, 60,'Select')
select_btn2 = button('#ABDEE6', 590, 220, 200, 60,'Select')
select_btn3 = button('#ABDEE6', 590, 320, 200, 60,'Select')
select_btn4 = button('#ABDEE6', 10, 320, 200, 60,'Select')
delay = 0
# Game loop
run = True
flag = False

loadAnimations()
while run == True:

    if not flag:
        draw_window()
        ss = sprite_sheet.SpriteSheet('Sprite Sheets\slime_spritesheet.png',(2000,4000))
        window.blit(ss.slime_preview(0),(10,10))
        window.blit(ss.slime_preview(5),(10,390))
        window.blit(ss.slime_preview(10),(590,390))
        window.blit(ss.slime_preview(15),(590,10))

    else:
        window.fill(bg)
        playAni(1)
    # Check input
    for event in pg.event.get():
        pos = pg.mouse.get_pos()

        if (event.type == QUIT):
            run = False

        if not flag:
            if pg.mouse.get_pressed()[0]:
                if select_btn1.over(pos):
                    mouse_click = True
                    select_btn1 = button('#ABDEE6', 10, 225, 200, 60,'Select')
                
                elif select_btn2.over(pos):
                    mouse_click = True
                    select_btn2 = button('#ABDEE6', 590, 225, 200, 60,'Select')
                
                elif select_btn3.over(pos):
                    mouse_click = True
                    select_btn3 = button('#ABDEE6', 590, 325, 200, 60,'Select')
                
                elif select_btn4.over(pos):
                    mouse_click = True
                    select_btn4 = button('#ABDEE6', 10, 325, 200, 60,'Select')
            else:
                if mouse_click == True:
                    mouse_click = False
                    flag = True
                    
    pg.display.update()
