


import math


def add(a,b):


	return a + b

add(3,4)







#subtracts a and b


def sub(a,b):


	return a - b
sub (5,3)











#A function that multiplies and b


def mul(a,b):


	return a*b
mul(4,4)










#A function that divides the float value 2.0 an 3 


def div(a,b):


	return a/b
div(2.0,3)










#this find  seconds to hours 


def Secondstohours(a,b,c):


	return a/b/c
Secondstohours(86400,60,60)










#finds area of a circle


def Areaofcircle(r):


	pi = (math.pi)


	return pi * r **2
Areaofcircle(5)


	





#A function that calculates the area of a circle


def Volumeofsphere(g):


	pi = (math.pi)


	return (((4/3.0)*pi)*g**3)
Volumeofsphere(5)










#A function that tells the volume of a sphere


def averagespherevolume(a,b):


	pi = (math.pi)


	x = a/2


	y = b/2


	Vol1 = Volumeofsphere(int(x))


	Vol2 = Volumeofsphere(int(y))


	return (Vol1 + Vol2)/2
averagespherevolume(10,20)










#tells you the area of a triangle


def trianglearea(a,b,c):


	d = (a+b+c)/2.0


	return math.sqrt(d*(d-a)*(d-b)*(d-c))
trianglearea(1,2,2.5)










# makes hello appear to the right 


def right_align(a):


	return (a.rjust(80))
right_align("hello")









def center(a):


	return (a.center(40))
center("hello")









def msg_box(x):


   return "+" + (len(x) + int(4)) * "-" + "+\n" "|" + "  " + x + "  " + "|\n" "+" + (len(x) + int(4)) * "-" + "+"







msg_box("hello")


msg_box("I eat cats")


#this uses the previously made variable msg box and uses i eat cats as the string in the variable 







z = add(4,6)


y = add(8,6)


print msg_box(str(z))


print msg_box(str(y))


x = sub(5,3)


w = sub(4,4)


print msg_box(str(x))


print msg_box(str(w))


v = mul(2,3.0)


u = mul(4,8)


print msg_box(str(v))


print msg_box(str(u))


t = div(48,8)


s = div(625,25)


print msg_box(str(t))


print msg_box(str(s))


r = Secondstohours(46890,60,60)


q = Secondstohours(60000,60,60)


print msg_box(str(r))


print msg_box(str(q))


p = Areaofcircle(6)


o = Areaofcircle(9)


print msg_box(str(p))


print msg_box(str(o))


n = Volumeofsphere(7)


m = Volumeofsphere(14)


print msg_box(str(n))


print msg_box(str(m))


l = averagespherevolume(20,40)


k = averagespherevolume(40,60)


print msg_box(str(l))


print msg_box(str(k))


j = trianglearea(2,2,2)


i = trianglearea(4,2,6)


print msg_box(str(j))


print msg_box(str(i))
#this put all the already determined variables into message boxes


















































