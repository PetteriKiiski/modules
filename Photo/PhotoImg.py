class SizeError:
	def __init__(self):
		print("""Bad size for width and height
SizeError""")
class InterpretError:
	def __init__(self):
		print("""Bad amount of inputs
InterpretError""")
class Photo:
	def __init__(self, width, height, *args):
		self.pixels = []
		self.width = width
		self.height = height
		if len(args) % 3 != 0:
			raise InterpretError()
		elif len(args) == width * height:
			raise SizeError()
		count = 0
		for pix in args:
			if not bool(count):
				self.pixels.append([])
			if count == 2:
				count = 0
			else:
				count += 1
			self.pixels[len(self.pixels) - 1].append(pix)
	def __list__(self):
		return self.pixels
	def __str__(self):
		return str(self.pixels)
	def open(self, file):
		hexadecimal = str()
		self.pixels = []
		strnum = str()
		right = False
		left = False
		try:
			with open(file, 'rt') as opening:
				for x in opening.read():
					if x == ' ':
						if not right:
							hexadecimal += '0'
						else:
							strnum += '0'
					if x == '!':
						if not right:
							hexadecimal += '1'
						else:
							strnum += '1'
					if x == '"':
						if not right:
							hexadecimal += '2'
						else:
							strnum += '2'
					if x == '#':
						hexadecimal += '3'
					if x == '$':
						hexadecimal += '4'
					if x == '%':
						hexadecimal += '5'
					if x == '&':
						hexadecimal += '6'
					if x == "'":
						hexadecimal += '7'
					if x == '(':
						hexadecimal += '8'
					if x == ')':
						hexadecimal += '9'
					if x == '*':
						hexadecimal += 'a'
					if x == '+':
						hexadecimal += 'b'
					if x == ',':
						hexadecimal += 'c'
					if x == '-':
						hexadecimal += 'd'
					if x == '.':
						hexadecimal += 'e'
					if x == '/':
						hexadecimal += 'f'
					if x == '@':
						self.pixels.append([])
						self.pixels[len(self.pixels) - 1].append(hexadecimal)
						hexadecimal = str()
						left = True
					if x == '>':
						left = False
						right = True
try:
	photo = Photo(3, 3, 'ff0000', 1, 1, '00ff00', 2, 1, '00ff00', 3, 1, '0000ff', 1, 1, 'ffff00', 1, 2, 'ff00ff', 2, 2, '00ffff', 3, 2, 'f0f0ff', 1, 3)
except SizeError:
	pass
except InterpretError:
	pass
print(str(photo))
