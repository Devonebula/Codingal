try:
    n=int(input("Enter your age:\t"))
    if n<18:
        raise ValueError("Your age is lesss than 18")
except ValueError as e:
    print(f"Error: {e}")
    