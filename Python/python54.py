import math
def cube(num):
    return math.pow(num, 3)
def check(num):
    if num % 3==0:
        return cube(num)
    else:
        return False
num=int(input("Enter a number:\t"))
print(check(num))