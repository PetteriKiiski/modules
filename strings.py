def myint(s):
	n = 0
	str_int = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	while s:
		n += 10 ** (len(s) - 1) * str_int[s[0]]
		news = ''
		for i in range(1, len(s)):
			news += s[i]
		s = news[:]
	return n
inp = input("Enter an integer: ")
print (myint(inp))
print (type(myint(inp)))
