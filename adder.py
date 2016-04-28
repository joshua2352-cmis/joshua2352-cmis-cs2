import math 

nothing = raw_input("next number:") 

def adder(total,nothing):


    nothing = raw_input("next number:") 
    if nothing == "":

        print "Goodbye"

    else: total += float(nothing) 
        
    adder()

def main():

    total = 0
    

    adder(total) 


main()




