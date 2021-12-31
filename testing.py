import circles, pygame, sys
from pygame.locals import *
canvas = pygame.display.set_mode((600, 600))
canvas.fill((255, 255, 255))
myCircle = circles.Circle(250, 250, 250)
image = pygame.image.load("../Games/Pygame/baddie.png")
size = 10
change = 0
while True:
	canvas.fill((255, 255, 255))
	canvas.blit(pygame.transform.scale(image, (size, size)), pygame.Rect(int(myCircle.get_next_point()[0]) + 50 - size // 2, int(myCircle.get_next_point()[1]) + 50, 50, 50))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
#	change += 0.15
#	if change > 1:
#		size += 1
#		change = 0
	pygame.display.update()
