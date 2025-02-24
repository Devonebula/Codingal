def digit_sum(start , iterations):
    num=start
    for i in range(iterations-1):
        num+=sum(int(k) for k in str(num))
        print(num)
        
digit_sum(23,11)
        