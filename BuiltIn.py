def integer_string(integer:int)->str:
	"""
	This function will convert an integer into a string
	Example 1:integer_string(55) = '55'
	Example 2:integer_string(23) = '23'
	Example 3:integer_string(16) = '16'
	This function can be usefull when you
	have an integer, but you need to use
	it like a string.
	"""
	output = ''
	#I believe I will need to contain the output until I have made the final decision.
	num = 1
	#I will also store the power of ten I am currently working on
	while True:
		if 10 ** num > integer:
			break
			"""
			Break out of the loop
			if the power of ten is bigger than the output
			for then I have the power of ten I want. Almost
			"""
		num += 1
		#Increase the power of ten for the next loop
	num -= 1
	#In the while loop, I increased the power of ten a little too much
	ilist = []
	# A list thats going to store all the different digits
	integer /= 10 ** num
	ilist += [integer]
	for x in range(0, num):
		integer *= 10
		#to get the next digit
		integer -= int(ilist[len(ilist) - 1]) * 10
		#remove the previous digit
		ilist += [integer]
		"""
		Adding the integer to the list in
		a way to add an item to a list
		which I preffer over the list.append(item) method"""
	for f in ilist:
		i = int(f)
		if i == 0:
			output += '0'
		if i == 1:
			output += '1'
		if i == 2:
			output += '2'
		if i == 3:
			output += '3'
		if i == 4:
			output += '4'
		if i == 5:
			output += '5'
		if i == 6:
			output += '6'
		if i == 7:
			output += '7'
		if i == 8:
			output += '8'
		if i == 9:
			output += '9'
	#go through all possible digits and put them into string
	return output
print (integer_string(15))
print (type(integer_string(15)))
print (ord('5'))
