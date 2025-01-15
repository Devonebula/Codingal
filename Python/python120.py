class Breed:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def display(self):
        print(f"name:{self.name}\nage:{self.age}\nbreed:{self.breed}")
class Dog:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"name:{self.name}")
    def show_breed(self):
        breed=input("Enter your breed:\t")
        age=int(input("Enter your age:\t"))
        dog=Breed(self.name, age, breed)
        dog.display()
dog1=Dog("kiku")
dog2=Dog("chiku")
dog1.show_breed()
dog2.show_breed()
