# Write a function is_prime(n) that checks if a number n is prime.
def isprime(n):
    if n>1:
        for i in range (2,(n//2)+1):
            if (n%i)==0:
                print("It is not a prime number")
                break
        else:
            print("It is a prime number")
    else:
        print("It is not a prime number")
isprime(int(input("Enter a number:\t")))
    
