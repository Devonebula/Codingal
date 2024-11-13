a=int(input("Enter the number of rows:\t"))
for i in range(a):
    for j in range(i+1):
        print("*", end=" ")
    print()