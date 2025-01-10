class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def display(self):
        print(f"name is {self.name}, max speed is {self.max_speed}, mileage is {self.mileage}")
class ship(vehicle):
    pass
c=ship("titanic", 100, 1000)
print(c.display())