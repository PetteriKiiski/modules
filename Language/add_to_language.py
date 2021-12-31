import random
definition = input("Word: ")
length = random.randint(3, 10)
vowels = ["a", "e", "i", "o", "u", "y"]
constanents = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
l = [vowels, constanents]
random.shuffle(l)
op = l
lan = ""
for i in range(0, length):
	lan += random.choice(op[i%2])
try:
	with open("language.lang", "r") as fh:
		txt = fh.read()
except EnvironmentError as err:
	print (err)
except Exception as err:
	print (err)
try:
	with open("language.lang", "w") as fh:
		fh.write(txt + "\n{0} = {1}".format(lan, definition))
except EnvironmentError as err:
	print (err)
except Exception as err:
	print (err)
