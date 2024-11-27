def total_bill(bill, tip):
    total= bill+(bill/100) * tip
    print(f"The total bill is {total}")
    
total_bill(int(input("Enter the bill\t")), float(input("Enter the tip percentage\t")))