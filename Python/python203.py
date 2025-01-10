class bird:
    def __init__(self, name):
        self.name = name
        print("Bird is ready")
    def whoisThis(self):
        print(f"This is {self.name}")
    def swim(self):
        print("Swim faster")
class penguin(bird):
    def __init__(self, name):
        bird.__init__(self, name)
        print("Penguin is ready")

koo=penguin("Koo")
koo.whoisThis()
koo.swim()
    
        