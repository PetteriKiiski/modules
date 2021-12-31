import random, pygame, sorting, time
from pygame.locals import *
class Mychar:
	def __init__(self, ch, locs):
		self.ch = ch
		self.locs = locs
def get_char():
	num_sym = random.randint(5, 10)
	locs = [[x, y] for x in range(0, 501) for y in range(0, 501)]
	syms = []
	for i in range(num_sym):
		sym = random.choice(locs)
		del locs[locs.index(sym)]
		syms += [sym]
	rlist = []
	for x in range(0, 501):
		rlist += [[]]
		for y in range(0, 501):
			rlist[-1] += [False]
	for i in syms:
		rlist[i[0]][i[1]] = True
	return Mychar(rlist, syms)
#	for x in range(0, 501):
#		rlist.append([])
#		for y in range(0, 501):
#			xs = [for i in locs]
#				rlist[-1].append(True)
#				continue
#			rlist[-1].append(False)
def display(char):
	ch = char.ch
	locs = char.locs
	canvas = pygame.display.set_mode((500, 500))
	canvas.fill((255, 255, 255))
	for x in range(0, 501):
		for y in range(0, 501):
			pygame.draw.rect(canvas, (0, 0, 0) if ch[x][y] else (255, 255, 255), pygame.Rect(x, y, 1, 1), 100)
	for loc in locs[1:]:
		pygame.draw.line(canvas, (0, 0, 0), locs[locs.index(loc) - 1], loc, 2)
	pygame.display.update()
	input()
def display_continus():
	canvas = pygame.display.set_mode((1360, 660))
	canvas.fill((255, 255, 255))
	syms = [[0, 0]]
#	for x in range(0, 100000):
#		syms += [[random.randint(0, 500), random.randint(0, 500)]]
#		pygame.draw.line(canvas, (0, 0, 0), syms[-2], syms[-1], 1)
#		pygame.display.update()
#	input()
#	return
	while True:
		syms += [[random.randint(0, 1360), random.randint(0, 660)]]
		pygame.draw.line(canvas, (0, 0, 0), syms[-2], syms[-1], 1)
		pygame.display.update()
		print ("waiting")
#		time.sleep(0.5)
#		if input() == "exit":
#			break
#	rlist = [True for x in range(0, 501) for y in range(0, 501) if [x, y] in syms else False]
display_continus()
#c = get_char()
#display(c)
