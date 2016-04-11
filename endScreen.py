import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from Button import Button
import os
import sys
import inputbox
import teststart

class endScreen:
	def __init__(self, screen,text):

		pygame.font.init()
		fontobject = pygame.font.Font(None,18)
		if pygame.mixer.music.get_busy():
			pygame.mixer.music.stop()
		pygame.mixer.music.load('Sound/bomb.mp3')
		pygame.mixer.music.play(-1, 0.0)
		if len(text) != 0:
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
						sys.exit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						if btnReplay.obj.collidepoint(mouse2):
							if pygame.mixer.music.get_busy():
								pygame.mixer.music.stop()
							print ("restart")
							teststart.start(screen)
						elif btnExit.obj.collidepoint(mouse2):
							if pygame.mixer.music.get_busy():
								pygame.mixer.music.stop()
							print ("exit")
							run1= False;
							sys.exit()
				btnReplay.draw(screen, mouse2, (150,(screen.get_height()-100),100,20), (150,(screen.get_height()-100)))
				btnExit.draw(screen, mouse2, (300,(screen.get_height()-100),100,20), (300,(screen.get_height()-100)))
				pygame.display.update()
				clock.tick(60)
