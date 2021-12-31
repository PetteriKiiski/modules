#Rule:If you don't want to type it all out:don't do it, there's probably a better way to do it
#Terrible
class Test1:
	def __init__(self):pass
	def repeat1(self):
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
class Test2:
	def __init__(self):pass
	def repeat2(self):
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
		print ("Hello")
#Bad
def repeat():
	print ("Hello")
	print ("Hello")
	print ("Hello")
	print ("Hello")
	print ("Hello")
	print ("Hello")
	print ("Hello")
	print ("Hello")
	print ("Hello")
	print ("Hello")
class Test1:
	def __init__(self):pass
	def repeat1(self):
		repeat()
class Test2:
	def __init__(self):pass
	def repeat2(self):
		repeat()
#Good
def sayHello():
	print ("Hello")
class Test1:
	def __init__(self):pass
	def repeat1(self):
		for i in range(0, 10):
			sayHello()
class Test2:
	def __init__(self):pass
	def repeat2(self):
		for i in range(0, 10):
			sayHello()
#Good
def sayHello():
	print ("Hello")
class Test:
	def repeat(self):
		for i in range(0, 10):
			sayHello()
class Test1(Test):
	pass
class Test2(Test):
	pass
