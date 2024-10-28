while True:

    a=int(input("Enter a number:\t"))
    b=int(input("Enter a number:\t"))
    c=int(input("Enter a number:\t"))


    if(a>0 or b>0 ):
        print("One the no. are psoitve")
    if(a<0 and b<0):
        print("Both the no. are nagative")
    if(a>0 and b<0):
        print("a is positive and b is negative")
    if(b>0 and a<0):
        print("b is positive and a is negative")
    if(a==0 or b==0 or c==0):
        print("One of the no. is zero")
    else:
        print("All numbers are zero")

