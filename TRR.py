import pygame
from pygame.locals import *
canvas = pygame.display.set_mode((500, 500))
canvas.fill((255, 255, 255))
def translation(right, up, *args):
	rvalue = []
	for arg in args:
		rvalue.append((arg[0] + right, arg[1] + up))
	return rvalue
def reflection(axis, *args):
	rvalue = []
	if axis == 'x':
		for arg in args:
			rvalue.append((arg[0], arg[1] * -1))
	elif axis == 'y':
		for arg in args:
			rvalue.append((arg[0] * -1, arg[1]))
	return rvalue
print (translation(3, 10, (5, 5), (10, 6), (9, 9), (5, 20)))
print (reflection('x', (5, 5), (10, 6), (9, 9), (5, 20)))
pygame.draw.polygon(canvas, (255, 0, 0), [(5, 300), (100, 6), (9, 9), (5, 20)])
pygame.draw.polygon(canvas, (0, 255, 0), translation(30, 100, (5, 300), (100, 6), (9, 9), (5, 20)))
while True:pygame.display.update()
