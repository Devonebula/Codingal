while True:
    cp=int(input("Enter the cost price:\t"))
    sp=int(input("Enter the selling price:\t"))
    if cp<sp:
        print(f"This is profit of {sp-cp} rs")
    else:
        print(f"This is loss of {cp-sp} rs")