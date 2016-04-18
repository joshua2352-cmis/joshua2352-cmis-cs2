import math 

def begin():
    print "This will find the average of stuuff"

def userinput(n1,n2,n3,n4,n5):
    n1=raw_input("what is the 1st number 0-10:")
    if int(n1)> 9 or int(n1)<1:
        wrong()
    n2=raw_input("what is the 2nd number 0-10:")
    if int(n2)> 9 or int(n2)< 1:
        wrong()
    n3=raw_input("what is the 3rd number 0-10:")
    if int(n3)> 9 or int(n3)< 1:
        wrong()
    n4=raw_input("what is the 4th number 0-10:")
    if int(n4)> 9 or int(n4)< 1:
        wrong()
    n5=raw_input("what is the 5th number 0-10:")
    if int(n5)> 9 or int(n5)<1:
        wrong()

def add(n1,n2,n3,n4,n5):
    averageX5 = int(n1) + int(n2) + int(n3) + int(n4) + int(n5)
def div(averageX5):
    average = int(averageX5) / 5

def wrong():
    print"that is not within range"

