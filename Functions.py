def add(a, b):
    return a + b
def sub (a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
 
a = add(9, 43)
b = sub(9, 43)
c = div(9, 43)
d = mul(9, 43)


print a 
print b 
print c
print d

def hours_from_seconds(seconds):
    hours = seconds / 3600
    return hours

hours = hours_from_seconds(86400)    
print hours

    

