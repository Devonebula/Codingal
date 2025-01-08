class iostring():
    def __init__(self):
        self.str=""
    def getstring(self):
        self.str=input("Enter a String:\t")
    def printstring(self):
        print(f" Result is: {self.str.upper()}")
k=iostring()
k.getstring()
k.printstring()