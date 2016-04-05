import pygame
import os
import sys
import inputbox
from errorScreen import errorScreen
from endScreen import endScreen
from pygame.locals import *

class animation3:
	def __init__(self,screen,direction,text,u1_,u2_,v1_,v2_):
		FPS = 30
		fpsClock = pygame.time.Clock()
		SCREEN_WIDTH = 600
		screen = pygame.display.set_mode((SCREEN_WIDTH,400), 0, 32)
		pygame.display.set_caption('Animation')
		WHITE = (255, 255, 255)
		RED = (255,0,0)
		background = pygame.image.load('Images/background.png')
		screen.blit(background,(0,0))
		textpos = text.get_rect()
		textpos.centerx = background.get_rect().centerx
		textpos.y = 350
		background.blit(text, textpos)
		objAImg = pygame.image.load('Images/game3/A.png')
		objBImg = pygame.image.load('Images/game3/B.png')

		fontObj = pygame.font.Font(None,16)
		objAImgx = 0
		objAImgy = 240
		objBImgx = 200
		objBImgy = 240
		Run1= True
		temp=1
		while Run1 :			#main game loop
			screen.blit(background,(0,0))
			
			if u1_ > 0:
				if u2_ == 0:
				
					if objAImgx <180 :
						objAImgx += 3
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
					#while temp<10:
					#	temp=temp+1
					#	print temp
					if objAImgx >= 180:
						Run1= False

#Final velocity animation nt wrking!

				elif u2_ < 0:
					if objAImgx >= objBImgx:
						Run1= False

					else :
						objAImgx += 3
						objBImgx -= 3
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
				else :


					if u2_ <u1_:
						objAImgx += 5
						objBImgx += 1
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))

					if objAImgx >= objBImgx:
						Run1= False
					
				
				
					if (u2_ >u1_) :
						objAImgx += 3
						objBImgx += 5
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
					if (u2_ == u1_) :
						objAImgx += 3
						objBImgx += 3
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))

					if objAImgx >= 620:
						endScreen(screen,"The blocks wont collide !")


						
						
					

			if u1_ == 0:
				if u2_ == 0:
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
				
					endScreen(screen,"The blocks wont collide !")

				if u2_ > 0:
					endScreen(screen,"The blocks wont collide !")

					


				elif u2_ < 0:
					if objAImgx >= objBImgx:
						Run1= False

					else :
						objAImgx += 5
						objBImgx -= 5
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
				else :
					if objAImgx >= objBImgx:
						Run1= False

					if u2_ <u1_:
						objAImgx += 5
						objBImgx += 5
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
					
						
			if u1_ >= 0:
				if u2_ == 0:
				
					if objAImgx <180 :
						objAImgx += 5
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
					#while temp<10:
					#	temp=temp+1
					#	print temp
					if objAImgx >= 180:
						Run1= False

				elif u2_ < 0:
					if objAImgx >= objBImgx:
						Run1= False

					else :
						objAImgx += 5
						objBImgx -= 5
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
				else :
					if objAImgx >= objBImgx:
						Run1= False

					if u2_ <u1_:
						objAImgx += 5
						objBImgx += 5
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
					
						


			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()
			fpsClock.tick(FPS)
		Run2= True
		collison = pygame.image.load('Images/game3/collison.jpg')
		screen.blit(collison,(0,0))
		pygame.display.update()
		fpsClock.tick(FPS)
		pygame.time.wait(3000)
		objAImgx = 180
		objAImgy = 240
		objBImgx = 220
		objBImgy = 240
		screen.blit(background,(0,0))
		screen.blit(objAImg, (objAImgx,objAImgy))
		screen.blit(objBImg, (objBImgx,objBImgy))
		pygame.display.update()
		fpsClock.tick(FPS)
		while Run2:
			screen.blit(background,(0,0))

			if v2_ > 0 and v1_ >0:
				if v1_ > v2_ :
	
					objAImgx += 5
					objBImgx += 3
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
				elif v1_ == v2_ :
	
					objAImgx += 4
					objBImgx += 4
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
				elif v1_ < v2_ :
	
					objAImgx += 3
					objBImgx += 5
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))

			elif v2_ > 0 and v1_ ==0:
				
				objBImgx += 4
				screen.blit(objAImg, (objAImgx,objAImgy))
				screen.blit(objBImg, (objBImgx,objBImgy))
			elif v2_ > 0 and v1_ <0:
				objAImgx -= 3
				objBImgx += 3
				screen.blit(objAImg, (objAImgx,objAImgy))
				screen.blit(objBImg, (objBImgx,objBImgy))
			elif v2_ == 0 and v1_ >0:
				objAImgx += 4
				
				screen.blit(objAImg, (objAImgx,objAImgy))
				screen.blit(objBImg, (objBImgx,objBImgy))
			elif v2_ == 0 and v1_ ==0:
				
				
				screen.blit(objAImg, (objAImgx,objAImgy))
				screen.blit(objBImg, (objBImgx,objBImgy))
			elif v2_ == 0 and v1_ <0:
				objAImgx -= 4
				
				screen.blit(objAImg, (objAImgx,objAImgy))
				screen.blit(objBImg, (objBImgx,objBImgy))
			elif v2_ < 0 and v1_ ==0:
				
				objBImgx -= 4
				screen.blit(objAImg, (objAImgx,objAImgy))
				screen.blit(objBImg, (objBImgx,objBImgy))
			elif v2_ < 0 and v1_ >0:
				objAImgx += 4
				objBImgx -= 4
				screen.blit(objAImg, (objAImgx,objAImgy))
				screen.blit(objBImg, (objBImgx,objBImgy))
			elif v2_ < 0 and v1_ <0:
				if v1_ > v2_ :
	
					objAImgx -= 3
					objBImgx -= 5
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
				elif v1_ == v2_ :
	
					objAImgx -= 4
					objBImgx -= 4
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))
				elif v1_ < v2_ :
	
					objAImgx -= 5
					objBImgx -= 3
					screen.blit(objAImg, (objAImgx,objAImgy))
					screen.blit(objBImg, (objBImgx,objBImgy))



			
			else :
				Run2 = False
			if objAImgx > 650 :
				errorScreen(screen,"Block will continue to move")

		
						
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
			fpsClock.tick(FPS)
			

