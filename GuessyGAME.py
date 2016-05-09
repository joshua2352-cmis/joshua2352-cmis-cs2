

import random

guesses = 0


number = random.randint(1, 100)
print(' i am thinking of a number between 1 and 100.')

while guesses < 6:
     print('whats your first guess')
     guess = input()
     guess = int(guess)

     guesses = guesses + 1

     if guess < number:
         print('Your guess is too low.') 

     if guess > number:
         print('Your guess is too high.')

     if guess == number:
         break

if guess == number:
     guessesTaken = str(guessesTaken)
     print('wow you must be a pshchic You guessed the number in ' + guesses + ' guesses!')

if guess != number:
     number = str(number)
     print('you are incorrect the number i was thinking of was ' + number)
