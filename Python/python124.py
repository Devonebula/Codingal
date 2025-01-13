class vehicle:
    def __init__(vehicleType):
        print(f"Vehicle type is {vehicleType}")
class car(vehicle):
    def __init__(self):
        print("car")
        super().__init__("Car")
class MotorCycle(vehicle):
    def __init__(self):
        
        print("MotorCycle")
        super().__init__("MotorCycle")
class Test():
    pass
print(issubclass(car,vehicle))
print(issubclass(MotorCycle,vehicle))
print(issubclass(Test,vehicle))
        