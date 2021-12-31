#72 lines long
#32 line long merge sort
#3 line min2
#3 line max2
def sortedFind(i, ints):
	sorted = ints[:]
	if len(sorted) == 0:
		return False
	if len(sorted) == 1:
		return sorted[0] == i
	mid = len(sorted) // 2
	if sorted[mid - 1] == i:
		return True
	if i > sorted[mid - 1]:
#		print (sorted[mid:])
		return find(i, sorted[mid:])
	else:
#		print (sorted[:mid])
		return find(i, sorted[:mid])
def find(i, ints):
	sorted = mergeSort(ints)
	if len(sorted) == 0:
		return False
	if len(sorted) == 1:
		return sorted[0] == i
	mid = len(sorted) // 2
	if sorted[mid - 1] == i:
		return True
	if i > sorted[mid - 1]:
#		print (sorted[mid:])
		return find(i, sorted[mid:])
	else:
#		print (sorted[:mid])
		return find(i, sorted[:mid])
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
	return sorted[-1]
def count(i, l):
	i_s = 0
	for x in l:
		if x == i:
			i_s += 1
	return i_s
