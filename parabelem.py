dollars = 1000
pennies = 0
for i in range(0, 30):
	pennies += 2 ** i
	print ("{0}:{1}".format(i + 1, pennies))
print ("{0} dollars, {1} pennies  (in dollars)".format(dollars, pennies / 100))
