import time
def ibin(n:int, as_string=False) -> list:
	def add(l):
		if 0 not in l:
			myl = [1]
			for i in l:
				myl.append(0)
			l = myl[:]
			return l
		if l[len(l) - 1] == 1:
			l = l[::-1]
			count = 0
			for i in l:
				if i == 0:
					l[count] = 1
					break
				if i == 1:
					l[count] = 0
				count += 1
			return l[::-1]
		else:
			l[len(l) - 1] += 1
			return l
	base = [0]
	value = 0
	while True:
		if value == n:
			break
		base = add(base)
		value += 1
	if not as_string:
		return base
	else:
		sbase = []
		for i in base:
			sbase.append(str(i))
		return ''.join(sbase)
t1 = time.time()
print (ibin(int(input("What do you want to convert to binary?: ")), True))
t2 = time.time()
print (t2 - t1)
