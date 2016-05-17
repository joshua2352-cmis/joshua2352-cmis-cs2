#Section 1: Terminology
# 1) What is a recursive function?
# a function that calls itself in itsself to repeat something 
#
#
# 2) What happens if there is no base case defined in a recursive function?
#it does nothing 
#
#
# 3) What is the first thing to consider when designing a recursive function?
# what will go in the base case 
#
#
# 4) How do we put data into a function call?
# tab it in then make a variable 
#
# 
# 5) How do we get data out of a function call?
#by making it do something and calling the function 
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 12
#a2 = 12 
#a3 =-1

#b1 = 9
#b2 = 2
#b3 =-2 

#c1 = -5
#c2 = -7
#c3 =24

#d1 = 6 
#d2 =8
#d3 =4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

import math 
import random 
#imports operators 

def adder(n1): 
	total = 0
	n1 = raw_input("next number:")
	if n1 == "":
		average = total2 / total  
		print 'the average of the odd numbers was {}' .format(average) + '.'
	else:
		return float(total) + 1 
		return float(total2) + n1 
		adder()
	

def main():
	adder(n1)
main()





	











