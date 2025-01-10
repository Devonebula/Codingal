class breed:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def display(self):
        print(f"name:{self.name}\nage:{self.age}\nbreed:{self.breed}")
class dog:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"name:{self.name}")
    def showbreed(self):
        breed=input("Enter your breed:\t")
        age=int(input("Enter your age:\t"))
        dog=breed(self.name, age, breed)
        dog.display()
dog1=dog("kiku")
dog2=dog("chiku")
dog1.showbreed()
dog2.showbreed()