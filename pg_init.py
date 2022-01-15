import pygame as pg
from pygame.locals import *


pg.init()
# Global variables for easy changes
screen_width = 1200
screen_height = 900
timer = None
window = None
fps = 30


bg = pg.Color(255,255, 255)
timer = pg.time.Clock()
window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("HackED")

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
			pg.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

		pg.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

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
    sprite_1.draw(window,(0,0,0))


sprite_1 = button((0,255,0), 0, 475, 225, 100,'Sprite 1')

# Game loop
end = False
while end == False:
    draw_window()
    pg.display.update()

    # Check input
    for event in pg.event.get():
        pos = pg.mouse.get_pos()

        if (event.type == QUIT):
            end = True

        if event.type == pg.MOUSEBUTTONDOWN:
            if sprite_1.over(pos) == MOUSEBUTTONDOWN:
                end = True   # select sprite 1
        
        if event.type == pg.MOUSEMOTION:
            if sprite_1.over(pos):
                sprite_1.color = (255,0,0)
            else:
                sprite_1.color = (0,255,0)

        # Update screen
        pg.display.update()
        timer.tick(fps)

