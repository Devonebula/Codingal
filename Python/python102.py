# Write a function factorial(n) that takes an integer n and returns its factorial. Handle edge cases for n = 0 and negative numbers.
import math
def factorial(n):
    if n<=0:
        print("Not Applicable")
    else:
        print( math.factorial(n))

factorial(int(input("Enter a number:\t")))
