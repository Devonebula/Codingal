a=(input("Which veichle do you want 1.Bike 2.Car:\t"))
if a=="1" or a=="Bike" or a=="bike":
    b=input("Which bike do you want: Bajaj, Yamaha or Honda:\t")
    print("Congratulations, you got", b)
elif a=="2" or a=="Car" or a=="car":
    b=input("Which Car do you want: Skoda, Honda or BMW:\t")
    print("Congratulations, you got", b)
else:
    print("Invalid input")