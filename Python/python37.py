a=int(input('Enter the starting range:\t'))
b=int(input('Enter the ending range:\t'))
if a>1:
    print(f"Prime numbers btw. {a} and {b} are:")

    for i in range(a,b+1):
    
        for j in range(2, i):
            if i%j==0:
                break;
        else:
            print(i, end=", ")
else:
    print("1 is not a prime number")
