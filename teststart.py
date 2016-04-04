
import pygame
import os
import sys
import inputbox
import demo
from Button import Button
from pygame.locals import *

pygame.init()
def start(DISPLAYSURF):
	btn = Button('Start')
	btn.setColor((255,0,0))
	btn.setHoverColor((0,255,0))
	btn.setFontColor((0,0,255))
	btn2 = Button('Credits')
	btn2.setColor((255,0,0))
	btn2.setHoverColor((0,255,0))
	btn2.setFontColor((0,0,255))
	clock = pygame.time.Clock()
	background=pygame.image.load('Images/simphy.jpg')
	run = True
	DISPLAYSURF = pygame.display.set_mode((600,400), 0, 32)
	while run:
		DISPLAYSURF.blit(background,(0,0))
		
 	   	#screen.blit(textSurfaceObj,textRectObj)
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if btn.obj.collidepoint(mouse):
					demo.startGame(DISPLAYSURF)			
				elif btn2.obj.collidepoint(mouse):
					pass
	
		btn.draw(DISPLAYSURF, mouse, (200,200,200,40), (225,203),40)
		btn2.draw(DISPLAYSURF, mouse, (200,250,200,40), (225,253),40)
		pygame.display.update()
		clock.tick(60)