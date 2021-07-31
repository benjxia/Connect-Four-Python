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
        declareWinner()
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
    #check every direction
    h = y
    c = column
    counth = 1
    while c > 0: #Checks left
        c-=1
        if turn == 1:
            if grid[y,c] != "X":
                break
            else:
                counth +=1
        if turn == 2:
            if grid[y,c] != "O":
                break
            else: 
                counth +=1
    c = column
    while c < xsize-1: #Checks Right
        c+=1
        if turn == 1:
            if grid[y,c] != "X":
                break
            else: 
                counth +=1
        if turn == 2:
            if grid[y,c] != "O":
                break
            else: 
                counth +=1
    c = column
    countv = 1
    while h < ysize-1: #Checks down
        h +=1
        if turn == 1:
            if grid[h,c] != "X":
                break
            else:
                countv+=1
        if turn == 2:
            if grid[h,c] != "O":
                break
            else:
                countv+=1     
    h = y  
    while h > 0: #Checks up
        h -= 1
        if turn == 1:
            if grid[h,c] != "X":
                break
            else:
                countv += 1
        if turn == 2:
            if grid[h,c] != "O":
                break
            else:
                countv += 1  
    h = y
    countur = 1 
    #count diagonally up and to the right, like NorthEast, idk what to call it lmao
    while c < xsize-1 and h > 0:
        c += 1
        h -= 1
        if turn == 1:
            if grid[h,c] != "X":
                break
            else: 
                countur += 1
        if turn == 2:
            if grid[h,c] != "O":
                break
            else: 
                countur += 1
    c = column
    h = y
    #count down and to the left
    while c > 0 and h < ysize -1:
        c -= 1
        h += 1
        if turn == 1:
            if grid[h,c] != "X":
                break
            else: 
                countur += 1
        if turn == 2:
            if grid[h,c] != "O":
                break
            else: 
                countur += 1
    c = column
    h = y

    countdr = 1
    #count down and to the right
    while c < xsize-1 and h < ysize-1:
        c += 1
        h += 1
        if turn == 1:
            if grid[h,c] != "X":
                break
            else: 
                countdr += 1
        if turn == 2:
            if grid[h,c] != "O":
                break
            else: 
                countdr += 1
    c = column
    h = y
    #count up and to the left
    while c > 0 and h > 0:
        c -= 1
        h -= 1
        if turn == 1:
            if grid[h,c] != "X":
                break
            else: 
                countdr += 1
        if turn == 2:
            if grid[h,c] != "O":
                break
            else: 
                countdr += 1
    if countdr >=4 or countur >=4 or counth >=4 or countv >=4:
        declareWinner()


def declareWinner():
    gameActive = False
    for i in range(5): print()
    print(grid)
    print(f"Player {turn} wins!")
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