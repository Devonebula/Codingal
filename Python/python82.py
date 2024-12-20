weather=(1,1,1,0,0,1,0,1,0)

a=0
b=0
for i in weather:
    
    
    if i==1:
        a+=1
    else:
        b+=1
        
        
if a>b:
    print("Sunny")
        
else:
    print("Rainy")