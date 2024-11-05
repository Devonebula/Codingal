a=input("Enter a Sring\t")
b=input("Enter the character to be searched\t")
c=0
f=0
for i in a:
    if b==i.upper() or b==i.lower():
        c=c+1   
        f=1

if f==0:
    print("Not found")
else:
    print(f"The count of {b} is {c}")