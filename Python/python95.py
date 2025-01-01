num1=[1,2,3]
num2=[4,5,6]

result=map(lambda x,y:x+y,num1,num2)

print(list(result))

nums=[1,2,3,4,5,6]
def sq(num):
    return num * num
square=list(map(sq,nums))
print(square)