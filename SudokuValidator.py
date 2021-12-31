#made by:peter
from sorting import *
class ParseError(Exception):pass
def validate(file:str)->bool:
	print ('NOTE: THERE IS A MUCH FASTER WAY TO DO THIS')
	try:
		with open(file, 'rt') as fh:
			text = fh.read()
	except:
		print ('Cannot Read File:{0}')
		return
	g = text.split('\n')
	if len(g) != 10:
		raise ParseError
	del g[len(g)-1]
	rows = g[:]
	col = []
	for i in range(0, 9):
		col.append([])
	for row in g:
		for i in range(0, 9):
			if not sortedFind('0123456789', row[i]):
				raise ParseError
			col[i].append(row[i])
	if len(col) != 9:
		raise ParseError
	boxs = []
	for i in range(0, 9):
		boxs.append([])
	for row in g[0:3]:
		boxs[0] += row[0:3]
		boxs[1] += row[3:6]
		boxs[2] += row[6:9]
	for row in g[3:6]:
		boxs[3] += row[0:3]
		boxs[4] += row[3:6]
		boxs[5] += row[6:9]
	for row in g[6:9]:
		boxs[6] += row[0:3]
		boxs[7] += row[3:6]
		boxs[8] += row[6:9]
	if len(boxs) != 9:
		raise ParseError
	prev = []
	for row in rows:
		for s in row:
			if find(int(s), prev):
				return False
			prev.append(int(s))
		prev = []
	for c in col:
		for s in c:
			if find(int(s), prev):
				return False
			prev.append(int(s))
		prev = []
	for box in boxs:
		for s in box:
			if find(int(s), prev):
				return False
			prev.append(int(s))
		prev = []
	return True
print (validate("Sudoku.dat"))
