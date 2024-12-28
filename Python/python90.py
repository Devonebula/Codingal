a={"Codingal":3, "is":2, "best":2, "for":2, "coding":1}
b=int(input("Enter the value you want to check:\t"))
c=0
for i in a:
    if a[i]==b:
        c=c+1
print(c) 