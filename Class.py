class ClassError(Exception):
	def __init__(self):
		print("Error: ClassError")
class PrivateError(ClassError):
	def __init__(self):
		print("""Error: Attribute is private
		PrivateError""")
class PrivateVariableError(PrivateError):
	def __init__(self):
		print("""Error: Class Variable is private
		PrivateVariableError""")
class PrivateMethodError(PrivateError):
	def __init__(self):
		print("""Error: Class Method is private
		PrivateMethodError""")
class CallError(ClassError):
	def __init__(self):
		print("""Error: Method must be called
		CallError""")
class Class:
	def __init__(self):
		self.privatekey = {}
		self.puvalues = {}
		self.prvalues = {}
		self.functions = []
	def __getitem__(self, iterator):
		try:
			iterator = str(iterator)
			if self.privatekey[iterator.replace("()", str())] == "private" or self.privatekey[iterator.replace("()", str())] == "private method":
				if iterator in self.functions:
					raise PrivateMethodError
				else:
					raise PrivateVariableError
			elif iterator.endswith("()"):
				exec(self.puvalues[iterator.replace("()", str())].split("return")[0])
				if "return" in self.puvalues[iterator.replace("()", str())]:
					I_AM_RETURNING_THIS_VALUE = self.puvalues[iterator.replace("()", str())].split("return")[1]
					return I_AM_RETURNING_THIS_VALUE
				else:
					return None
			else:
				if iterator in self.functions:
					raise CallError
				else:
					return self.puvalues[iterator.replace("()", str())]
		except ClassError:
			pass
	def create_private(self, name, value):
		self.privatekey[name] = "private"
		self.prvalues[name] = value
	def create_public(self, name, value):
		self.privatekey[name] = "public"
		self.puvalues[name] = value
	def create_private_method(self, name, code):
		self.privatekey[name] = "private method"
		self.puvalues[name] = code
		self.functions.append(name)
	def create_public_method(self, name, code):
		self.privatekey[name] = "public method"
		self.puvalues[name] = code
		self.functions.append(name)
