#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# it is  used to set the value of a variable
#(correct)
#
#2 3pts) Write a technical definition for 'function'
#you put in a set of values a set of values come out (like a vending machine in a sense)
#(correct)
#
#3 1pt) What does the keyword "return" do?
# causes your function to exit and hand back a value to its caller. The point of functions in general is to take in inputs and return something. The return statement is used when a function is ready to return a value to its caller.
#(correct)
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: float  (float)(2.0) (3.0)
#	2: strings  (str)  ("hello") ("23")
#	3: integers (int)   (3) (5)
#	4:  boolean (bool) True , False (==)(!<) 
#	5: list [,]:['a',1,1.3]
#(4/5)
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# a function definition is what the function does while a function call uses the function
#(2/2)
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:integer
#	2:float value is basically an integer but with a decimal point 
#	3:string , is a word or has letter value 
#(0/3)
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi


import math
#imports math 

C1 = raw_input("Area of C1: ")
C2 = raw_input("Area of C2: ")
C3 = raw_input("Area of C3: ")
#give promps to the user
def circle_diameter(area):
    return math.sqrt(((area) / math.pi)) + math.sqrt(((area) / math.pi))
#this tells the system what to do 
print ""

CC1 = math.sqrt(((float(C1)) / math.pi)) + math.sqrt(((float(C1)) / math.pi))
CC2 = math.sqrt(((float(C2)) / math.pi)) + math.sqrt(((float(C2)) / math.pi))
CC3 = math.sqrt(((float(C3)) / math.pi)) + math.sqrt(((float(C3)) / math.pi))
#this makes the equation and sets up the steps for it 
Total = float(CC1) + float(CC2) + float(CC3)
C3 = float(CC3)
C2 = float(CC2)
C1 = float(CC1)
#this changes the values in the answer to float values
print "Circle  Diameter"
print "c1      " + str(C1)
print "c2      " + str(C2)
print "c3      " + str(C3)
print "Totals  " + str(Total)
#this makes shows you the answer to the equation
#(24/25)
#missing main -1
