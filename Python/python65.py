try:
    n1=int(input("Enter first number:\t"))
    n2=int(input("Enter second number:\t"))
    result=n1/n2
except ZeroDivisionError as e:
    print(f"Error: {e}")
    
except ValueError as e:
    print(f"Error: {e}")
    
except ArithmeticError as e:
    print(f"Error: {e}")
    
except SyntaxError as e:
    print(f"Error: {e}")
except:
    print("Something went wrong")
finally:
    print("It will definetly run")
    
    