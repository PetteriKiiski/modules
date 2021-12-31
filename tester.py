import math2
try:
	print (math2.factorial(input()))
except MemoryError:
	print ('You gave a too big number, I do not know how to calculate it')
