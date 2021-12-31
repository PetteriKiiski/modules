import pygame, sys, json
from pygame.locals import *
#Set up pygame
pygame.init()
canvas = pygame.display.set_mode((1360, 660))
try:
	with open("MoneyTracker.json", "rb") as fh:
		Info = json.load(fh)
except EnvironmentError as err:
	print ("1{}".format(err))
while True:
	canvas.fill((255, 255, 255))
	for i in range(0, len(Info)):
#		x = i * 10
		if i == 0 or Info[i - 1] < Info[i]:
			color = (0, 255, 0)
		elif Info[i - 1] == Info[i]:
			color = (0, 0, 255)
		else:
			color = (255, 0, 0)
		pygame.draw.rect(canvas, color, pygame.Rect(i - 5, 660 - (Info[i] - 5), 10, 10))
		if i != 0:
			pygame.draw.line(canvas, color, (i-10, 660 - (Info[i-1] - 5)), (i-5, 660 - (Info[i] - 10)))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
