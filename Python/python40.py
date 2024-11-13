a=int(input("Enter the number of rows:\t"))
num=1
for i in range(a):
    for j in range(i+1):
        print(num, end=" ")
        num+=1
    print()