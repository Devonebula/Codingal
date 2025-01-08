class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"name:{self.name}\nsalary:{self.salary}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"name:{self.name}\nage:{self.age}")
    def changetoemployee(self):
        sallary=float(input("Enter your salary:\t"))
        employee=Employee(self.name,sallary)
        employee.display()
keshav=Person("keshav",13)
keshav.changetoemployee()