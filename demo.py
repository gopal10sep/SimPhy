import pygame
import os
import sys
import inputbox
from Button import Button
from animation import animation
from animation2 import animation2
from errorScreen import errorScreen
from pygame.locals import *
import game1
import game2
from game3 import *
pygame.init()

#if __name__ == '__main__':
def startGame(DISPLAYSURF):	
	#now Displaying first DISPLAYSURF, what need to be calculated
	background=pygame.image.load('Images/home.jpg')
	#DISPLAYSURF = pygame.display.set_mode((600,400))
	DISPLAYSURF.blit(background,(0,0))
	pygame.mixer.music.load('Sound/bill1.mid')
	pygame.mixer.music.play(-1, 0.0)
	try:
		btngame1=Button('Linear Motion')
		btngame2=Button('Vertical Motion')	
		btngame3=Button('Momentum')	
		clock = pygame.time.Clock()
		run1= True;
		while run1:
			DISPLAYSURF.blit(background,(0,0))
			mouse2 = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run1 = False
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if btngame1.obj.collidepoint(mouse2):
						game1.startGame1(DISPLAYSURF)
					elif btngame2.obj.collidepoint(mouse2):
						game2.startGame2(DISPLAYSURF)
					elif btngame3.obj.collidepoint(mouse2):
						print ("game 3")
			if run1 == True:
				btngame1.draw(DISPLAYSURF, mouse2, (100,210,150,20), (100,210))				# draw linear motion button
				btngame2.draw(DISPLAYSURF, mouse2, (300,210,150,20), (300,210))				# draw vertical motion button
				btngame3.draw(DISPLAYSURF, mouse2, (200,310,150,20), (200,310))	
				pygame.display.update()
				clock.tick(60)
	except :							# except is the python equivalent of catch block
		print ("error in demo")
		errorScreen(DISPLAYSURF,"Something went wrong")
