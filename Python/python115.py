class employee:
    def __init__(self):
        print("A Employee is created")
    def __del__(self):
        print("A Employee is deleted")
    def print_info(self):
        print("Dummy text")
def create_obj():
    print("Creating an object")
    emp = employee()
    print("Function completed")
    return emp
print("Calling the function")
obj=create_obj()
obj.print_info()
print("Program completed")