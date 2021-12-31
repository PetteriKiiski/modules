import pickle, random, sys
all_chars2 = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '*', '-', 'q', 'w', 'e', 'r', 't', \
	'y', 'u', 'i', 'o', 'p', '[', '\\', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 'v', \
	'b', 'n', 'm', ',', '.', '/']
all_chars1 = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '*', '-', 'q', 'w', 'e', 'r', 't', \
	'y', 'u', 'i', 'o', 'p', '[', '\\', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 'v', \
	'b', 'n', 'm', ',', '.', '/']
d = {}
for i in all_chars1:
	choice = random.choice(all_chars2)
	d[i] = choice
	del all_chars2[all_chars2.index(choice)]
print (d)
try:
	with open(sys.argv[1], 'wb') as fh:
		pickle.dump(d, fh)
except Exception as err:
	print ('Cannot open file:{0}'.format(err))
