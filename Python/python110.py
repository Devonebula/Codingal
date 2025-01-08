class veichle:
    def __init__(self, max_speed, mileage, model):
        self.max_speed = max_speed
        self.mileage = mileage
        self.model = model
    def info(self):
        print(f"max speed is {self.max_speed}, mileage is {self.mileage}, model is {self.model}")
audia5 = veichle(200, 10, "Audi A5")
audia5.info()
bmw7=veichle(300, 20, "BMW 7")
bmw7.info()