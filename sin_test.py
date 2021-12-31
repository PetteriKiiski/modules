import math, pygame, derivative
from pygame.locals import *
pairs = []
zoom = float(input("How much zoom?: "))
canvas = pygame.display.set_mode((1000, 1000))
canvas.fill((255, 255, 255))
def myfunc(x):
	return 0.5 * x
def mycos(x):
	return math.cos(x)
#for i in range(0, 360):
#	pairs += [[i, math.sin(i)]]
for i in range(0, 360):
	pairs += [[i, derivative.derivate(mycos)(i)]]
#for i in range(0, 360):
#	pairs += [[i, math.tan(i)]]
#print (pairs)
#pygame.draw.line(canvas, (0, 0, 0), (0, 250), (500, 250))
for pair in pairs:
	pygame.draw.rect(canvas, (255, 0, 0), pygame.Rect((pair[0] - 5) * zoom, (zoom - pair[1] - 5) * zoom, 10, 10))
#	print (pygame.Rect((pair[0]) * 10, (200 - pair[1]) * 10, 1, 1))
#print ("Done displaying")
while True:
	canvas.fill((255, 255, 255))
	for pair in pairs:
		pygame.draw.rect(canvas, (255, 0, 0), pygame.Rect((pair[0] - 5) * zoom, (zoom - pair[1] - 5) * zoom, 10, 10))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		if event.type == KEYDOWN:
			if event.key == K_DOWN and zoom > 1:
				zoom -= 1
			elif event.key == K_DOWN:
				zoom /= 2
			if event.key == K_UP and zoom < 1:
				zoom *= 2
			if event.key == K_UP:
				zoom += 1
	pygame.display.update()
