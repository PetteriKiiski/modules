#Rules:
#1.If token is ALIVE and has more than 3 ALIVE tokens around it, it DIES of overcrowding
#2.If token is ALIVE and has less than 2 ALIVE tokens around it, it DIES of loneliness
#3.If tokin is ALIVE and has 2 or 3 ALIVE tokens around it, it stays ALIVE
#4.If token is DEAD and has 3 ALIVE tokens around it, it comes back to LIFE
#Note:
#True is an alive token
#False is a dead token
#And please be fair:make a same side by same side grid input.
def GameOfLife(position): #Define GameOfLife with position arument
	r_list = [] #Return value list
	for x in range(len(position) + 2): #loop all x for the return list
		r_list += [[]] #Add to the return value list an empty list
		for y in range(len(position[0]) + 2): #loop all y for the return list
			r_list[-1] += [None] #Add None to the return list
	for x in range(-1, len(r_list)): #loop all positions on the old and return boards
		if x in [-1, len(r_list) - 1]: #if x is in the return list: ...
			for y in range(0, len(r_list)-1):
				if x == -1:
					new_x = x + 1
				else:
					new_x = x
GameOfLife([[False, False, False, False, False], [False, True, True, True, True], [False, False, False, True, True], [False, False, False, False, True], [False, False, False, False, False]])
