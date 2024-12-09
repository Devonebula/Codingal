import random
playing = True 
life=3
a=random.randint(1,10)
while playing:
    print(f"You have {life} chances")
    if life==0:
        print("You lost all your chances")
        print("The number was",a)
        want=int(input("If you want to play again press 1 otherwise press 0"))
        if want==1:
            life=3
            a=random.randint(1,10)
        elif want==0:
            print("Thanks for playing")
            break
        
    else:        
        b=int(input("Enter your guess from 1 to 10:\t"))
        if b==a:
            print("You won")
        else:
            print("Wrong Guess")
            life-=1
            
