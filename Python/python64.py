try:
    a=int(input("Enter a number:\t"))
except ValueError as e:
    print(f"Exeption {e}")