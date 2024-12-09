import random
chances=["rock","paper","scissor"]
a=random.choice(chances)
while True:
    b=input("Enter your choice:\t").lower()
    if b=="rock" and a=="scissor" or b=="paper" and a=="rock" or b=="scissor" and a=="paper":
        print("You won")
    elif a==b:
        print("It's a draw")
    else:
        print("You lost")
        print("The computer chose",a)
    c=int(input("If you want to play again press 1 otherwise press 0:\t"))
    if c==0:
        print("Thanks for playing")
        break
    else:
        a=random.choice(chances)
        
        