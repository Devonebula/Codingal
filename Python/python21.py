while True:
    a=int(input("Number of units consumed:\t"))
    if a<=50:
        bill=a*2.60+25
    elif a>50 and a<=100:
        bill=50*2.60+(a-50)*3.25+35
    elif a>100 and a<=200:
        bill=50*2.60+50*3.25+(a-100)*5.26+45
    elif a>200:
        bill=50*2.60+50*3.25+100*5.26+(a-200)*8.45+75
        
    print(f"The bill is {bill}₹")
            