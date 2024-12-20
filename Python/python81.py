r=(1,2,3,3,2,1)
s=0
e=len(r)-1
while s<e:
    if r[s] != r[e]:
        print("Not a palindrome")
        break
    s+=1
    e-=1
else:
    print("It is a palindrome")
