import pygame
import inputbox
from pygame.locals import *
from animation3 import animation3
pygame.init()

class Button:
   def __init__(self, text):
      self.text = text
      self.is_hover = False
      self.default_color = (100,100,100)
      self.hover_color = (255,255,255)
      self.font_color = (0,0,0)
      self.obj = None
      
   def label(self):
      '''button label font'''
      font = pygame.font.Font(None, 20)
      return font.render(self.text, 1, self.font_color)
      
   def color(self):
      '''change color when hovering'''
      if self.is_hover:
         return self.hover_color
      else:
         return self.default_color
         
   def draw(self, screen, mouse, rectcoord, labelcoord):
      '''create rect obj, draw, and change color based on input'''
      self.obj  = pygame.draw.rect(screen, self.color(), rectcoord)
      screen.blit(self.label(), labelcoord)
      
      #change color if mouse over button
      self.check_hover(mouse)
      
   def check_hover(self, mouse):
      '''adjust is_hover value based on mouse over button - to change hover color'''
      if self.obj.collidepoint(mouse):
         self.is_hover = True 
      else:
         self.is_hover = False
         
if __name__ == '__main__':
			
	FPS = 30
	fpsClock = pygame.time.Clock()
	SCREEN_WIDTH = 600
	DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,400), 0, 32)
	pygame.display.set_caption('Animation')
	WHITE = (255, 255, 255)
	RED = (255,0,0)

	btn = Button('Input the values')
	
	clock = pygame.time.Clock()
	background=pygame.image.load('Images/game1.jpg')

	run = True
	
	while run:
		DISPLAYSURF.blit(background,(0,0))
		#cloud = pygame.image.load('Images/cloudf.png')
 	   	#DISPLAYSURF.blit(textSurfaceObj,textRectObj)
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if btn.obj.collidepoint(mouse):
					countInputs=1;
					u1 = inputbox.ask(DISPLAYSURF, "Initial velocity of object 1, u1",countInputs)
					u1_ = float (u1)
					countInputs=countInputs+5;
					u2 = inputbox.ask(DISPLAYSURF, "Initial velocity of object 2, u2",countInputs)
					u2_ = float (u2)
					countInputs=countInputs+5;
					m1 = inputbox.ask(DISPLAYSURF, "Mass of object 1, m1",countInputs)
					m1_ = float (m1)
					countInputs=countInputs+5;
					m2 = inputbox.ask(DISPLAYSURF, "Mass of object 2, m2",countInputs)
					m2_ = float (m2)
					#countInputs=countInputs+5;
					#a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					#a2 = float (a1)
					#countInputs=countInputs+5;
					#t1 = inputbox.ask(DISPLAYSURF, "Time, t",countInputs)
					if(m1<0 or m2<0):
						errorScreen(DISPLAYSURF,"Invalid datas entered")
					#t2 = float (t1)
					v1 = (((m1_ - m2_)*u1_) + (2*m2_*u2_))/(m1_+m2_)
					v1_ = str (v1)
					v2 = ((2*m1_*u1_) - (( m1_ - m2_)* u2_))/(m1_+m2_)
					v2_ = str (v2)
	
					objAImg = pygame.image.load('Images/game3/A.png')
					objBImg = pygame.image.load('Images/game3/B.png')
					#cloud = pygame.image.load('Images/cloudf.png')
					#tree = pygame.image.load('Images/tree.png')
					background = pygame.image.load('Images/background.png')
					DISPLAYSURF.blit(background,(0,0))
					font = pygame.font.Font(None, 20)
					text = font.render("Final Velocity of object A ="+v1_+"metre/sec and Final Velocity of object B ="+v2_+"metre/sec", 1, (10, 10, 10))
					textpos = text.get_rect()
					textpos.centerx = background.get_rect().centerx
					textpos.y = 350
					background.blit(text, textpos)
					
					#treex=370
					#treey = 0
					#catx = 0
					#caty = 240
					#textpos = text.get_rect()
					#textpos.centerx = background.get_rect().centerx
					#textpos.y = 350
		
					#background.blit(text, textpos)


					#cloudx = SCREEN_WIDTH + 5
					#cloudy = 60
					#centerx = SCREEN_WIDTH
					#fontObj = pygame.font.Font(None,16)
					#textSurfaceObj = fontObj.render('Block is going to infinity!!',True,RED)
					#textRectObj = textSurfaceObj.get_rect()
					#textRectObj.center = (centerx,5)
					animation3(DISPLAYSURF,'right',text,u1_,u2_,v1_,v2_)
					run = False

					
										
               
				
				
		btn.draw(DISPLAYSURF, mouse, (185,80,200,20), (225,83))

		pygame.display.update()
		clock.tick(60)
