def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:  
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def countEmpty(board):
    printBoard(board)
    rowEmpty = [0] * 9
    colEmpty = [0] * 9
    gridEmpty = [[0] * 3 for _ in range(3)]
    
    emptyPositions = []
    
    for r in range(9):
        for c in range(9):
            if int(board[r][c]) == 0:  #the board was being sent as a string from the js
                rowEmpty[r] += 1
                colEmpty[c] += 1
                gridEmpty[r // 3][c // 3] += 1
                emptyPositions.append((r, c))
    
    #print("Empty positions before sorting:", emptyPositions)
    
    def priority(pos):
        r, c = pos
        return min(rowEmpty[r], colEmpty[c], gridEmpty[r // 3][c // 3])
    
    emptyPositions.sort(key=priority)

    #print("Sorted empty positions:", emptyPositions)
    
    return emptyPositions