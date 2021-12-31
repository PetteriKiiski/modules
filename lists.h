//32 lines long
bool find(i, ints):
	sorted = mergeSort(ints);
	if (len(sorted) == 0)
	{
		return false;
	}
	if (len(sorted) == 1)
	{
		return sorted[0] == i;
	}
	mid = len(sorted) / 2
	if sorted[mid - 1] == i:
		return True
	if i > sorted[mid - 1]:
#		print (sorted[mid:])
		return find(i, sorted[mid:])
	else:
#		print (sorted[:mid])
		return find(i, sorted[:mid])
def myfind(i, ints):
	for j in ints:
		if j == i:
			return True
	return False
def mergeSort(ints):
	if len(ints) == 0:
		return ints
	if len(ints) != 2 and len(ints) != 1:
		mid = len(ints) // 2
		list1 = ints[mid:]
		list2 = ints[:mid]
		var1 = mergeSort(list1)
		var2 = mergeSort(list2)
		ptr1 = 0
		ptr2 = 0
		rvalue = []
		while True:
			if var1[ptr1] < var2[ptr2]:
				rvalue.append(var1[ptr1])
				ptr1 += 1
				if ptr1 == len(var1):
					rvalue += var2[ptr2:]
					break
			else:
				rvalue.append(var2[ptr2])
				ptr2 += 1
				if ptr2 == len(var2):
					rvalue += var1[ptr1:]
					break
		return rvalue
	else:
		if len(ints) == 1:
			return ints
		if len(ints) == 2:
			if ints[0] < ints[1]:
				return ints
			return ints[::-1]
def min2(l):
	sorted = mergeSort(l)
	return sorted[0]
def max2(l):
	sorted = mergeSort(l)
	return sorted[::-1]
def mysort(l):
	copyl = l
	empty = []
	for y in range(0, len(copyl)):
		for x in copyl:
			if x == min(copyl):
				del copyl[copyl.index(x)]
				empty.append(x)
	return empty
l = []
for i in range(10000, 0, -2):
	l.append(i)
#print (min2([7, 8, 9, 1, 11, 10, 9, 8, 7]))
#print (mergeSort([6, 5, 8, 1, 5, 10, 7]))
#print (find(10, [6, 5, 8, 1, 5, 10, 7]))
#print (find(2000, l))
