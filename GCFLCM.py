import sorting
def GCF(n1, n2):
	list1 = []
	list2 = []
	for i in range(1, (n1 // 2 if n1 > n2 else n2 // 2) + 1):
		if n1 % i == 0:
			list1 += [i]
		if n2 % i == 0:
			list2 += [i]
	list1 = list1[::-1]
	list2 = list2[::-1]
	for i in list1:
		if sorting.find(i, list2):
			return i
def LCM(n1, n2):
	list1 = []
	list2 = []
	for i in range(1,n2+1):
		list1 += [n1*i]
	for i in range(0,n1+1):
		list2 += [n2*i]
	for i in list1:
		if sorting.find(i, list2):
			return i
	return n1 * n2
print (LCM(int(input("What is the first number you want to find: ")), int(input("What is the second number you want to find: "))))
