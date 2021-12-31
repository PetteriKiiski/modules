import time
def primes(endAt):
	start = 0
	isPrime = True
	while True:
		for i in range(2, start):
			if start % i == 0:
				isPrime = False
		if isPrime:
			yield start
		start += 1
		if start == endAt + 1:
			break
		isPrime = True
def isPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return (False, i)
	return True
counter = 0
for x in primes(1000000):
	print (x)
