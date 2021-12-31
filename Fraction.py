#imports my module named 'GCFLCM'
import GCFLCM
#Error class raised if the denominator is 0
class DenominatorError(Exception):
#Initializer function for the Denominator Error, takes a string for a parameter
	def __init__(self, err:str):
#Displays the error message
		print (err)
#Creates MixedNumber class
class MixedNumber:
#Initializer function for the MixedNumber class, takes the whole number part(default 0), numerator, denominator, and if the fraction is negative or not(default False)
	def __init__(self, whole:int, numerator:int, denominator=None, negative:bool = False):
#if the denominator parameter is None, since we cannot say that the whole variable default is 0 strait away...
		if denominator == None:
#Then set the denominator to the numerator
			denominator = numerator
#numerator the the whole number
			numerator = whole
#And since the default for the whole number is 0, set it to zero
			whole = 0
#if the denominator is 0...
		if denominator == 0:
#raise the DenominatorError with an error message of "DenominatorError:Cannot have denominator as 0"
			raise DenominatorError("DenominatorError:Cannot have denominator as 0")
#Sets self.whole to whole
		self.whole = whole
#self.denominator to denominator
		self.denominator = denominator
#self.numerator to numerator
		self.numerator = numerator
#and self.negative to negative
		self.negative = negative
#__add__ special method to use the '+' operator among MixedNumbers, takes a MixedNumber as a parameter
	def __add__(self, mixedNumber:MixedNumber)->MixedNumber:
#Sets the original return value that will be modified later in the function
		rvalue = MixedNumber(self.whole + mixedNumber.whole, 0, 1)
		if self.denominator != mixedNumber.denominator:
			denominator = LCM(self.denominator, mizedNumber.denominator)
			mixedNumber1 = MixedNumber(self.whole, self.numerator*(denominator/self.denominator),denominator,self.negative)
			mixedNumber2 = MixedNumber(mixedNumber.whole, mixedNumber.numerator*(denominator/mixedNumber.denominator),denominator,mixedNumber.negative)
		else:
			mixedNumber1 = MixedNumber(self.whole, self.numerator, self.denominator, self.negative)
			mixedNumber2 = mixedNumber(mixedNumber.whole, mixedNumber.numerator, mixedNumber.denominator, mixedNumber.negative)
		rvalue.numerator = mixedNumber1.numerator + mixedNumber2.numerator
		rvalue.denominator = mixedNumber1.denominator
		return rvalue
