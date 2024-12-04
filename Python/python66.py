valid=False
while not valid:
    try:
        a=int(input("Enter a number:\t"))
        while a%2==0:
            print("Bye Bye")
        valid=True
    except ValueError as e:
        print(f"Error: {e}")