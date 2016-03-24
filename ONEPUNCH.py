import math

import random


Minimum = int(raw_input("What's the minimum number? "))


Maximum = int(raw_input("What's the maximum number? "))


print "I'm thinking of a number from " + str(Minimum) + " to " + str(Maximum) + "."

Guess = str(raw_input("What do you think it is?: "))

def CorrectORincorrect():

   x = number = random.randint(Minimum, Maximum)

   if int(x) == int(Guess):

       print """

The target was {}
Your guess was {}
That's correct! You must be a SAIKOU HEROOOOOOOOOO!

		""".format(str(x), str(Guess))

   elif str(x) > str(Guess):

       tolow = int(x) - int(Guess)

       print """

The target was {}
Your guess was {}
That's under by {}

		""".format(str(x), str(Guess), tolow)

   elif str(x) < str(Guess):

       tohigh = int(Guess) - int(x)

       print """

The target was {}
Your guess was {}
That's over by {}

		""".format(str(x), str(Guess), tohigh)

CorrectORincorrect()
