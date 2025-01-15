class bmw:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed
    def fuel_type(self):
        print(f"fuel type is {self.fuel_type}")
    def max_speed(self):
        print(f"max speed is {self.max_speed}")
class ferrari:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed
    def fuel_type(self):
        print(f"fuel type is {self.fuel_type}")
    def max_speed(self):
        print(f"max speed is {self.max_speed}")

bmww=bmw("petrol",200)
ferrariw=ferrari("petrol",300)

tup=(bmww,ferrariw)
for i in tup:
    i.fuel_type()
    i.max_speed()
        