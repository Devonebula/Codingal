import random
d=""
for i in range(3):
    a=random.choice(["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"])
    b=random.choice(["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"])
    c=random.choice([1,2,3,4,5,6,7,8,9,0])
    d+=a
    d+=b
    d+=str(c)
print(d)

