try:
    a=int(input("Enter your age:\t"))
    if a%2==0:
        print("Your age is even")
    else:
        print("Your age is odd")
except ValueError as e:
    print(f"Error: {e}")
