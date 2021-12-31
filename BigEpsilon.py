class EquationError:pass
def bigepsilon(stop, n, eq):
	eq = eq.rstrip()
	rvalue = 0
	if isinstance(stop, int):
		while n != stop:
			rvalue += eval(eq)
			n += 1
	elif stop == 'infinite':
		for i in range(0, 1000):
			rvalue += eval(eq)
			n += 1
	return rvalue
def factorial(n):
	value = 1
	if n == 0:
		return 0
	for i in range(1, n):
		value *= i
	return value
print (bigepsilon(5, 0, 'n'))
print (factorial(100))
