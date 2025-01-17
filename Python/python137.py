import random

class fruitquiz:
    def __init__(self, name):
        self.name=name
        self.fruits={
            "Apple":"red",
            "Banana":"yellow",
            "Cherry":"red",
            "Watermelon":"green",
            "Orange":"orange",
            "Strawberry":"red"
        }
    def quiz(self):
        while True:
            print(f"Welcome {self.name}")
            fruit,color=random.choice(list(self.fruits.items()))
            print(f"What is the color of {fruit}?")
            ans=input("Enter the color:\t").lower()
            if ans==color:
                print("You are right")
            else:
                print("You are wrong")
            option=int(input("Enter 1 to continue and 0 to exit:\t"))
            if option==0:
                print("Thanks for playing")
                break
print("Wolcome to my Fruit Quiz")
obj=fruitquiz(input("Enter your name:\t"))
obj.quiz()
