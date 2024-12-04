import random
def treasure_hunt_game():
    grid_size=5
    treasureX, treasureY=random.randint(0,grid_size-1),random.randint(0,grid_size-1)
    attempts=0
    
    print("Welcome to the treasure hunt Game!")
    print("You have to find the treasure within this 5x5 grid box")
    print("Your treasure is in the {treasureX} row and {treasureY} column".format)
    print("Enter your guesses as row and coloumn separated by a space")

    while True:
        try:
            guess=input("Enterr yor guess (row column): ").split()
            if guess=="-1":
                print("You quit the game")
                break
            
            
            row, col=map(int, guess.split())
            if row<0 or row>=grid_size-1 or col<0 or col>=grid_size:
                print("Invalid Row and Column")
                continue



        except ValueError:
             print("Invalid input kindly enter the two numbers separated by a space")
             continue