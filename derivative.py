#lim h -> 0
#2a2y3⇒ h′(b)=6a2b2
import math
h = 0.000000000000001
def testfunc(x, y):
	return 2 * x + x * y ** 2
def derivate(func):
	def outfunc(x):
		return (func(x + h) - func(x)) / h
	return outfunc

def partial_derivate(func, numparams):
	def outfunc(*params):
		if len(params) != numparams:
			return
		return (func(params[0] + h, *params[1:]) - func(*params[0:])) / h
	return outfunc
mytestfunc = partial_derivate(testfunc, 2)
print (mytestfunc(0, 2), mytestfunc(3, 2))
#excpects:~4, ~4
