def numbers(num):
    if num==11:
        return
    else:
        print(num)
        numbers(num+1)
numbers(1)

def numbers(num):
    if num==0:
        return
    else:
        print(num)
        numbers(num-1)
numbers(10)