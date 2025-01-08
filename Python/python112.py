class student:
    def __init__(self, name , age , grade , marks, marks2, marks3):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks
        self.marks2 = marks2
        self.marks3 = marks3
    def average(self):
        print(f"The average marks is {(self.marks + self.marks2 + self.marks3 )/ 3}")
    def display(self):

        print(f"My name is{self.name}, my age is{self.age}, my grade is{self.grade} and my average is {keshav.average()}")

keshav=student("keshav", 13, 8, int(input("Enter marks:\t")), int(input("Enter marks:\t")), int(input("Enter marks:\t")))
keshav.display()
        
        