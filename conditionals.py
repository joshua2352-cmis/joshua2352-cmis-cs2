import math 
import random 


def stage2():
	BOSS=raw_input("a large room looms ahead with a Giant lock and you have the key you have maxed out all your stats and know what lies ahead do you enter or knock enter/knock")

	knock = True 

	enter = False 

	if BOSS == "knock":

		print "a knight 10 times you size roughly opens the door you back up a few feet then stand your ground the knight apreciating that you were respectful and knocked he throws a medium power hit if you roll above a 3 you block the attack and move into the attack phase and slay the knightif you roll a 3 or below you fall to the knight and your journey ends"
		ROLL1()

	elif BOSS == "enter": 

		print " you silently enter and sneak up a knight 10 times your size you attack like a coward but he notices the swing he begins to move if you roll above a 5 your attack hits the knight and he falls in you roll a 5 or below the knight slays you"
		ROLL2()

def ROLL1():
	roll = random.randint(1,6)


	if roll > 3:
		print 'you have rolled a {}'.format(roll) + ' you slay the knight in one blow after rolling away from his attack' 

	elif roll < 4: 
		print' you have rolled a' .format(roll)+ ' you try to dodge but end up getting hit YOU DIED'
def ROLL2():
	roll2 = random.randint(1,6)


	if roll2 > 5:
		print 'you have rolled a {}'.format(roll) + ' you slay the knight in one blow after you sword hits the knight ' 

	elif roll2 < 6: 
		print' you have rolled a' .format(roll)+ ' you try to hit but end up missing  he turns around and hits you YOU DIED'
		


def cABBAGE():	
	fight=raw_input("you are attacked by cute flying cabbages do you fight yes/no:")
	yes = True
	no = False
	if fight == "yes": 

		print "luck is on your side you slay the cabbages fiercly and gain 1,000,000 Baht you set off to anothertown to buy high level armor and run into a giant mechanical spider it looms threateningly over you and starts to attack"

	elif fight == "no":
		print "you run away like a little girl and meet a giant mechanical spider it looms threateningly over you and starts to attack"
	else:
		print "HS"
def Spider():
	fight2 = raw_input("the spider is threatening to crush your city and your home do you fight or run fight/run:") 
	if fight2 == "run":
		print "You made the right choice leave this fight to the higher level players"
		stage2()

	elif fight2 == "fight" :
		print "you are trampled by the spider and your journey ends here" 
	else:
		print "you choose neither and decided to enjoy the show and watch as your friends fall to spider you then chuckle to yourself and eat a bit of your cabbage friend that you kept it softly cries you chuckle a little more."

def main():
	cABBAGE()
	Spider()
	
main()



