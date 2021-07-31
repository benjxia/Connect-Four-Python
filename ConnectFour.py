import numpy as np
import sys


turn  = 1# 1 = Player 1 (X), 2 = Player 2 (O)
xsize = 7
ysize = 7
grid = np.empty([ysize,xsize],dtype = str)
for i in range(xsize):
    grid[0,i] = i+1
for y in range(1,ysize):
    for x in range(0,xsize):
        grid[y,x] = " "


def main(): 
    global turn
    turn = 1
    global grid
    gameActive = True
    while(gameActive):
       cycle()


def cycle():
    global turn
    for i in range(5): print()
    print(grid)
    askColumn()
    turn = 2 if turn == 1 else 1


def askColumn():
    column = int(input(f"Player {turn}- Choose Column: ")) - 1
    if column == 745979:
        print("Cheat Code Activated")
        declareWinner(turn)
    else:
        for y in reversed(range(ysize)):
            if grid[1,column] != " ":
                for i in range(5): print()
                print(grid)
                print("Error: Column is full")
                askColumn()
                break
            elif grid[y,column] == " ":
                grid[y,column] = "X" if turn == 1 else "O"
                checkState(y, column)
                break

    
def checkState(y, column):
    #check left/right
    horizontal = y
   # while horizontal >= 0: #Check left

def declareWinner(i):
    gameActive = False
    print(f"Player {i} wins!")
    LastMessage = input("Type 'Exit' to end Connect-4, type anything else to reset: ")
    if LastMessage.lower().replace(" ","") == "exit":
        sys.exit()
    else:
        reset()
        

def reset():
    for y in range(1,ysize):
        for x in range(0,xsize):
            grid[y,x] = " "
    main()


main()
