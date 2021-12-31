import time
def randint(end:int):
	end += 1
	seed = time.time()
	orig_seed = time.time()
	seed *= end
	seed -= orig_seed
	seed **= (orig_seed % 15)
	orig_seed = time.time()
	seed %= end
	seed += orig_seed
	seed **= (orig_seed % 15)
	seed %= end
	return int(seed)
if __name__ == '__main__':
	def count(l, val):
		count = 0
		for i in l:
			if i == val:
				count += 1
		return count
vals = []
print (randint(10))
