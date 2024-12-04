a=float(input("Enter the amount:\t"))
b=float(input("How much you have paid:\t"))
c=b-a
if c<0:
    print("You have to pay more money")
else:
    print(f"Change is {c}")
    