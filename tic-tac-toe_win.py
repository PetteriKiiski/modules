#challenges:
#Restrictions (
#len(args) == width
#len(args[i]) == dimension
#)
#Number 1:Defaults
#dimension:2
#width:3
#Number 2:Defaults
#dimension:2
#width:3
#Number 2:Defaults
#dimension:2d
#Number3:Defaults
def WinFunc(*args):
	c_args = args[:]
	passes = [False, False]
	for i in range(2):
		numList = [arg[i] for arg in args]
		numList.sort()
		if (numList[0] == numList[2] + 2 or numList[0] == numList[2] - 2)
	if all(passes):
		return True
	return False
print (WinFunc((1,1), (2,2), (3,3)))
