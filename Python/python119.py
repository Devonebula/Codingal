class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

c = circle(float(input("Enter the radius:\t")))
print("Area of circle is:\t", c.area())
print("Perimeter of circle is:\t", c.perimeter())