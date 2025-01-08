class student:
    def __init__(self, name , age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display(self):
        print(f"name is {self.name}, age is {self.age}, grade is {self.grade}")
    
keshav=student("keshav", 13, 10)
keshav.display()
        