import math
import random
class EncryptSoh:
	def __init__(self, text):
		self.text = ''
		for s in text:
			self.text += str(math.sin(ord(s))) + '.'
			print (ord(s))
	def get_text(self):
		return self.text
print (EncryptSoh('~').get_text())
