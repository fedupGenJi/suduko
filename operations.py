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
    
    for r in range(len(board)):
        for c in range(len(board[0])):
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

def valid(board, number, position):
    number = str(number)

    #check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    
    #check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
        
    #check 3*3 box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == number and (i,j) != position:
                return False
    
    return True

def solver(board, emptyBoxes):
    if not emptyBoxes:
        return True
    
    find = emptyBoxes[0]
    row, col = find
            
    for j in range(1,10):
        if valid(board, j, (row,col)):
            board[row][col] = str(j)
            if solver(board, emptyBoxes[1:]): #slices the first element
                return True
            board[row][col] = "0"
    
    return False