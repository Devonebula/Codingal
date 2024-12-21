import math

a=int(input("Enter the starting number:\t"))
b=int(input("Enter the ending number:\t"))
for i in range(a,b+1):
    a=i*i
    print(i,":",a)
    if a%2==0:
        print("The square of",i,"is even")
    else:
        print("The square of",i,"is odd")