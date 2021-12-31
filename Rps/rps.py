#Rock Paper Scizors Shoot attempted AI
import json
try:
	with open("rps.json", "r") as fh:
		pattern_d = json.load(fh)
		if pattern_d == None:
			pattern_d = {"pattern":[1], "index":0}
except Exception as err:
	print ("Errno[1]:{}".format(err))
	exit()
guess = pattern_d["pattern"][pattern_d["index"]]
while True:
	guess_u = input("Guess Rock, Paper or Scizors(1, 2 or 3 ): ")
	print ()
	if guess == guess_u:
		print ("Tie-(breaker)!")
		continue
	if guess_u == guess - 1:
		print ("You Lose1")
	elif guess - 1 == 0 and guess_u == 3:
		print ("You Lose2")
	else:
		print ("You Win")
	break
