num=input("Enter a number:\t")
l=len(num)
q=int(num)
sum=0
while q>0:
    r=q%10
    sum=sum+(r**l)
    q=q//10
if sum==int(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")