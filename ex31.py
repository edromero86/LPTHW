print "You enter a dark room with two doors. Do you go through door 1 or door 2?"
print "Type: 1 or 2"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Too Bad! GAME OVER!!"
	elif bear == "2":
		print "The bear eats your legs off. Too Bad! GAME OVER!!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		
elif door == "2":
	print "You stare into the endless abyss of a maze."
	print "Choose 1 - 3."
	print "1. Blueberries."
	print "2. Yellow Jacket clothespins."
	print "3. Understand revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		
else: 
	print "You stumble around and fall on a knife and die. Game Over!"


		