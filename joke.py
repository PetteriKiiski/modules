#A "random" module for shuffling lists
import threading, time
ValsLock = threading.Lock()
timingLock = threading.Lock()
timing = True
class ShuffleThread(threading.Thread):
	def __init__(self, val, rand, time):
		super().__init__()
		self.val = val
		self.rand = rand
		self.time = time
	def run(self):
		print ("ONLINE")
		while True:
			with timingLock:
				if timing == False:
					break
			print (timing)
			time.sleep(self.time)
		with ValsLock:
			self.rand += [self.val]
def randomize(l):
	rand = []
	for thread in range(0, len(l)):
		c_thread = ShuffleThread(l[thread], rand, thread)
		c_thread.daemon = False
		c_thread.start()
	timing = False
	while len(rand) != len(l):
		pass
#		print (rand)
	return rand
print (randomize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

