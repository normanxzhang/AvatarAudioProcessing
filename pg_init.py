import pygame as pg
from pygame.locals import *
import sprite_sheet
import animation as ani
import pyaudio
import audio

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
    green_idle = ss.loadRow(1)
    green_talking = ss.loadRow(2)

    blue_idle = ss.loadRow(6)
    blue_talking = ss.loadRow(7)

    red_idle = ss.loadRow(11)
    red_talking = ss.loadRow(12)
    
    yellow_idle = ss.loadRow(16)
    yellow_talking = ss.loadRow(17)

    animations.append(ani.Animation("Idle", green_idle, 80))
    animations.append(ani.Animation("Talking", green_talking, 40))
    
    animations.append(ani.Animation("Idle", blue_idle, 80))
    animations.append(ani.Animation("Talking", blue_talking, 40))
    
    animations.append(ani.Animation("Idle", red_idle, 80))
    animations.append(ani.Animation("Talking", red_talking, 40))

    animations.append(ani.Animation("Idle", yellow_idle, 80))
    animations.append(ani.Animation("Talking", yellow_talking, 40))




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
            font = pg.font.SysFont('corbel', 40)
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
    

select_btn1 = button('#ABDEE6', 70, 205, 200, 60,'Select')
select_btn2 = button('#ABDEE6', 530, 205, 200, 60,'Select')
select_btn3 = button('#ABDEE6', 530, 485, 200, 60,'Select')
select_btn4 = button('#ABDEE6', 70, 485, 200, 60,'Select')
delay = 0
# Game loop
run = True
flag = False
loadAnimations()
audioManager = audio.Audio(1024, pyaudio.paInt16, 1, 44100, 0.03)
audioManager.init()
green_flag = False
blue_flag = False
red_flag = False
yellow_flag = False


while run == True:
    if not flag:
        draw_window()
        ss = sprite_sheet.SpriteSheet('Sprite Sheets\slime_spritesheet.png',(2000,4000))
        window.blit(ss.slime_preview(0),(70,-5))
        window.blit(ss.slime_preview(5),(70,275))
        window.blit(ss.slime_preview(10),(530,275))
        window.blit(ss.slime_preview(15),(530,-5))

    else:
        
        if(audioManager.talking):
            if green_flag:
                window.fill('#FF0000')
                playAni(1)
            elif blue_flag:
                window.fill('#7F00FF')
                playAni(7)
            elif red_flag:
                window.fill('#00FF00')
                playAni(5)
            elif yellow_flag:
                window.fill('#FFA500')
                playAni(3)
        else:
            if green_flag:
                window.fill('#FF0000')
                playAni(0)
            elif blue_flag:
                window.fill('#7F00FF')
                playAni(6)
            elif red_flag:
                window.fill('#00FF00')
                playAni(4)
            elif yellow_flag:
                window.fill('#FFA500')
                playAni(2)

    # Check input
    for event in pg.event.get():
        pos = pg.mouse.get_pos()

        if (event.type == QUIT):
            run = False

        if not flag:
            if pg.mouse.get_pressed()[0]:
                if select_btn1.over(pos):
                    mouse_click = True
                    select_btn1 = button('#ABDEE6', 70, 210, 200, 60,'Select')
                    green_flag = True
                
                elif select_btn2.over(pos):
                    mouse_click = True
                    select_btn2 = button('#ABDEE6', 530, 210, 200, 60,'Select')
                    blue_flag = True
                
                elif select_btn3.over(pos):
                    mouse_click = True
                    select_btn3 = button('#ABDEE6', 530, 490, 200, 60,'Select')
                    red_flag= True

                elif select_btn4.over(pos):
                    mouse_click = True
                    select_btn4 = button('#ABDEE6', 70, 490, 200, 60,'Select')
                    yellow_flag = True

            else:
                if mouse_click == True:
                    mouse_click = False
                    flag = True
                    
    pg.display.update()
    audioManager.listen()

audioManager.close()
