import random
import time

number=random.randint(1,100)

def intro():
    print("MAY I HAVE YOUR NAME?\n")
    global name
    name = input()
    print(name+",we are going to play a game. I am thinking of a number between 1 and 100.")
    if number % 2 == 0:
        x="even"
    else:
        x="odd"
    print(f"This is an {x} number.")
    time.sleep(.5)
    print("Go ahead and guess the number.")
def pick():
    guessesTaken =0
    while guessesTaken < 6:
        time.sleep(.25)
        enter=input("Guess:")
        try:
            guess=int(enter)
            if guess<=100 and guess>=1:
                guessesTaken += 1