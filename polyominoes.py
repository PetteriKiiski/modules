def polyminoes(x):
	def recursion(inputlist, inputnum):
		sizeofgrid = len(inputlist[0]) + 1
		if sizeofgrid > inputnum:
			return inputlist
		orig_grid = []
		for x in range(sizeofgrid):
			for y in range (sizeofgrid):
				orig_grid[-1][y] = False
			orig_grid += [[]]
		
	recursion([[[True]]], x)
def rotate_polyominoe(polyominoe):
	
