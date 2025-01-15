class vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity
        self.fare_price=self.seating_capacity*100
class bus(vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)
        self.fare_price=self.seating_capacity*100
    def final_price(self):
        return self.fare_price+(10/100*self.fare_price)

bus1=bus(50)
print(bus1.final_price())
