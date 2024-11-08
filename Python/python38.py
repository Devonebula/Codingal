a=(input("Enter a number of lenght greater than two:\t"))
b=len(a)
p=1
if b>2:
    if b%2==0:
        q=b//2
        p=int(a[q])*int(a[q-1])*p
    else:
        q=b//2
        p=p*int(a[q])
    print(f"The product of middle two or one objects is {p}")
else:
    print("The number is less than hundred")

