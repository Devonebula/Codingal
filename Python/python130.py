from abc import ABC, abstractmethod

class shape(ABC):
    def __init__(self, figure, color, area):
        self.figure = figure
        self.color = color
        self.area = area
    def display(self):
        pass
    
class circle(shape):
    def __init__(self, figure, color, area, radius):
        super().__init__(figure, color, area)
        self.radius = radius
    def display(self):
        print(f"I am {self.figure} with color {self.color} and my area is {self.area}")
class square(shape):
    def __init__(self, figure, color, area, side):
        super().__init__(figure, color, area)
        self.side = side
    def display(self):
        print(f"I am {self.figure} with color {self.color} and my area is {self.area}")

a=float(input("Enter the radius of circle:\t"))
b=float(input("Enter the side of square:\t"))
c=circle("circle", "red", 3.14*a*a,a )
d=square("square", "blue", b*b, b)
c.display()
d.display()
