a=input("Enter a string:\t")
b= input('Which character do you want to count:\t')
c=0
d=False
for i in a:
    if i==b:
        d=True
        c=c+1
if d==True:
    print("Character is found and the occurence is", c)
else:
    print("Character is not found")