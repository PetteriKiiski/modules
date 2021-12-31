import re
IsElementCompound = re.compile(r"^([a-zA-Z]{1,2}\d*)+$")
IsElement = re.compile(r"^(?P<element>[A-Z]{1}[a-z]?\d*)$")
if __name__ == "__main__":
	print (IsElement.match("H2").group('element'))
