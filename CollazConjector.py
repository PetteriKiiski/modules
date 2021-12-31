import sys
def Collaz(num):
	print (num)
	greatest = num
	loops = 0
	while True:
#		print (num)
		if num == 1:
			break
		loops += 1
		if num % 2 == 0:
			num //= 2
		else:
			num *= 3
			num += 1
		if num > greatest:
			greatest = num
	print ("Number of loops: {}".format(loops))
	print ("Highest number: {}".format(greatest))
#for x in range(1, 100):
Collaz(int(sys.argv[1]))
