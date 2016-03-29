import math 
def div(no1,b,y,x):
    answer=(float(b) * int(y) / int(x))
    return answer

def user(b,y,x,no1):
    actualanswer = div(no1,b,y,x)
    out = """
    print for (b) you put {}
    for (y) you put {}
    for (x) you put {} 
    the answer is {}
    your comment was {}
    """.format(b,y,x,actualanswer,no1)
    return out


def main():
    no1 = raw_input("this will find the answer to a simple equation any comments:")
    b = raw_input("enter first numero this will be the number being divided i.e b:")
    y = raw_input("enter second number this will be the number dividing i.e y:")
    x = raw_input("enter third number this will be what b * y /x will equal enter any number")    
    function = div(no1,b,y,x)
    function2 = user(b,y,x,no1)
    print function2

main()
    


    
