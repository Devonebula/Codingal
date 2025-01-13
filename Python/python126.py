class computer:
    def __init__(self):
        self.name="Dell"
        self.__maxprice=900
    def sell(self):
        print("Name:",self.name)
        print("Max price:",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price
        print("Price Updated Alert ")
    
c=computer()
c.sell()
print("----"*15)
c.__maxprice=1000
c.sell()
print("----"*15)
c.setmaxprice(1000)
c.sell()