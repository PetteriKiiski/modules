import sorting
def FuzzySelectSpace(Img, seed):
	seed_id = Img[seed[0]][seed[1]]
	seeds = [seed]
	try:
		if Img[seed[0] - 1][seed[1]] == seed_id:
			seeds += FuzzySelectSpace(Img, [seed[0] - 1, seed[1]])
	except IndexError:
		pass
	try:
		if Img[seed[0] + 1][seed[1]] == seed_id:
			seeds += FuzzySelectSpace(Img, [seed[0] + 1, seed[1]])
	except IndexError:
		pass
	try:
		if Img[seed[0]][seed[1] - 1] == seed_id:
			seeds += FuzzySelectSpace(Img, [seed[0], seed[1] - 1])
	except IndexError:
		pass
	try:
		if Img[seed[0]][seed[1] + 1] == seed_id:
			seeds += FuzzySelectSpace(Img, [seed[0], seed[1] + 1])
	except IndexError:
		pass
	rseeds = []
	for i in range(min(rseeds), max(rseeds) + 1):
		if sorting.count(i, seeds) > 0:
			rseeds += [i]
	return rseeds
l = [["a", "a", "a", "a", "a"], ["a", "a", "a", "a", "b"], ["a", "a", "a", "b", "b"], ["a", "a", "b", "b", "c"], ["a", "b", "b", "c", "c"]]
points = FuzzySelectSpace(l, [0, 0])
for point in points:
	print (l[point[0]][point[1]])
