board={"7":" ", "8":" ", "9":" ",
       "4":" ", "5":" ", "6":" ",
       "1":" ", "2":" ", "3":" "
       }

board_keys=[]

for key in board:
    board_keys.append(key)

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn="X"
    count=0
    
    for i in range(10):
        print_board(board)
        print("It's your turn," + turn+ ".Move to which place?")
        move = input("Enter your move (1-9):\t")
        if board[move]==" ":
            board[move]=turn
            count+=1
        else:
            print("Sorry, this place is already occupied.\n Move to which place?")
            continue
        if count>=5:
            
            if board["7"]== board["8"]==board["9"]!=" ":
                print_board(board)
                print("\n Game Over.\n")
                print(" **** " +turn+ " won **** ")
                break

            elif board["4"]== board["5"]==board["6"]!=" ":
                print_board(board)
                print("\n Game Over.\n")
                print(" **** " +turn+ " won **** ")
                break
            elif board["1"]== board["2"]==board["3"]!=" ":
                print_board(board)
                print("\n Game Over.\n")
                print(" **** " +turn+ " won **** ")
                break
            
            
            elif board["7"]== board["4"]==board["1"]!=" ":
                print_board(board)
                print("\n Game Over.\n")
                print(" **** " +turn+ " won **** ")
                break
            elif board["8"]== board["5"]==board["2"]!=" ":
                print_board(board)
                print("\n Game Over.\n")
                print(" **** " +turn+ " won **** ")
                break
            elif board["9"]== board["6"]==board["3"]!=" ":
                print_board(board)
                print("\n Game Over.\n")
                print(" **** " +turn+ " won **** ")
                break
            
            
            elif board["7"]== board["5"]==board["3"]!=" ":
                print_board(board)
                print("\n Game Over.\n")
                print(" **** " +turn+ " won **** ")
                break
            elif board["1"]== board["5"]==board["9"]!=" ":
                print_board(board)
                print("\n Game Over.\n")
                print(" **** " +turn+ " won **** ")
                break
            
        if count==9:
            print("\n Game Over.\n")
            print("It's a Tie!!")
        if turn=="X":
            turn="O"
        else:
            turn="X"
        
    restart = input("Do you want to play Again?(y/n):\t")
    if restart=="y" or restart=="Y":
        for key in board_keys:
            board[key]=" "
        game()
game()