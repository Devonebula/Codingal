decimal_number = int(input("Enter a decimal number: "))

binary = ""

while decimal_number > 0:
    remainder = decimal_number % 2
    binary = str(remainder) + binary  
    decimal_number //= 2


if binary == "":
    binary = "0"

print(f"The binary representation is: {binary}")
