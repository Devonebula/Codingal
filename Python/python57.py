    
def shutdown():
    a=input("Press yes for shutdown\t,no for not shutdown:\t")
    if a=="yes" or a=="Yes":
        print("Shutting down")
    elif a=="no" or a=="No":
        print("Not shutting down")
    else:
        print("Invalid input")

shutdown()