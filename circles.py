import math
class Circle:
	def __init__(self, radius:float, center_x:float, center_y:float):
		self.degree = 0.000
		self.radius=radius
		self.x=center_x
		self.y=center_y
	def __generator_for_degrees(self):
		base = 0.0
		while True:
			yield base
			base += 0.01
			if base == 360:
				break
	def get_points(self):
		rvalue = [None, None]
		for alpha in self.__generator_for_degrees():
			yield [self.x + self.radius * math.cos(alpha), self.y + self.radius * math.sin(alpha)]
	def get_next_point(self):
		rvalue = [None, None]
		self.degree += 0.01
		return [self.x + self.radius * math.cos(self.degree), self.y + self.radius * math.sin(self.degree)]
if __name__ == '__main__':
	pygame = __import__('pygame')
	sys = __import__('sys')
	#import pygame
	#import sys
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	canvas = pygame.display.set_mode((500, 500))
	canvas.fill(WHITE)
	circle = Circle(250, 250, 250)
	counter = 0
	for point in circle.get_points():
		point[0] = int(point[0])
		point[1] = int(point[1])
		pygame.draw.rect(canvas, BLACK, pygame.Rect(point[0], point[1], 1, 1))
		pygame.display.update()
		counter += 1
#		print (counter)
	print ('done')
	while True:
		pass
