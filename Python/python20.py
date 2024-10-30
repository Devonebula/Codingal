
while True:
    a=input("Do you have any Medical Problems:\t")
    if a=="Yes" or a=="yes":
        print("You can take the exam")
    elif a=="No" or a=="no":
        b=int(input("Enter your attendance:\t"))
        if b>=75:
            print("You can take your exam")
        else:
            print("You cannot take the exam")
    else:
        print("Invalid input")