red = int(input('Number of red frogs: '))
green = int(input('Number of green frogs: '))
var = green + 1
counter = 0
n = 2
while n > red:
	counter += green + 1
	n += 1
print (counter + var)
