import math
try:
    a=int(input("Enter the number:\t"))
    print(f"The sin of the number is {math.sin(a)}")
    print(f"The cos of the number is {math.cos(a)}")
    print(f"The tan of the number is {math.tan(a)}")
except ValueError as e:
    print(f"Error: {e}")
