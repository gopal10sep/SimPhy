import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from Button import Button
import os
import sys
import inputbox
import teststart
pygame.init()

class errorScreen:
	def __init__(self, screen,text):
	    # set up music
		pygame.mixer.init()
		pygame.mixer.music.load('Sound/error.mp3')
		pygame.mixer.music.play(-1, 0.0)
		pygame.font.init()
		fontobject = pygame.font.Font(None,18)
		if text!=':)':
			bckgd = pygame.image.load('Images/error.jpg')
			screen.blit(bckgd,(0,0))
		if text != ':)':
			pygame.draw.rect(screen, (75,100,25),((screen.get_width() / 2) - 100,100,200,20), 0)
			pygame.draw.rect(screen, (255,255,255),((screen.get_width() / 2) - 102,98,204,24), 1)
		if len(text) != 0:
			if text != ':)':
				screen.blit(fontobject.render(text, 1, (255,255,255)),((screen.get_width() / 2) - 100, 100))
				pygame.display.flip()
			btnReplay = Button('  Play Again ?')
			btnExit = Button('          Exit' )
			clock = pygame.time.Clock()
			run1= True;
			run2= False;
			while run1:
				mouse2 = pygame.mouse.get_pos()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						if pygame.mixer.music.get_busy():
							pygame.mixer.music.stop()
						pygame.quit()
						run1 = False
						sys.exit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						if btnReplay.obj.collidepoint(mouse2):
							if pygame.mixer.music.get_busy():
								pygame.mixer.music.stop()
							print ("restart")
							teststart.start(screen)
						elif btnExit.obj.collidepoint(mouse2):
							print ("exit")
							if pygame.mixer.music.get_busy():
								pygame.mixer.music.stop()
							run1= False;
							sys.exit()
							
				btnReplay.draw(screen, mouse2, (150,(screen.get_height()-100),100,20), (150,(screen.get_height()-100)))
				btnExit.draw(screen, mouse2, (300,(screen.get_height()-100),100,20), (300,(screen.get_height()-100)))
				pygame.display.update()
				clock.tick(60)
