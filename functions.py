def minesCoordinates(rows, columns, mines):
    '''
    This function will assign the coordinates of each mine.
    The number of rows, columns and mines are integers that have been defined in start.py.
    If the length of the list is greater than one, check for any duplicates.
    If duplicate found, remove the one with the greatest index number (which is j).
    checkForDuplicates is used because if a duplicate is found, only two mines will have the same coordinates.
    This function will return a list with the coordinates of each mine.
    '''
    from random import randint
    cellsWithMines = []
    counter = 0

    while counter < mines:
        cellsWithMines.append([randint(1, rows), randint(1, columns)])

        if len(cellsWithMines) > 1:
            checkForDuplicates = True
            for i in range(len(cellsWithMines)):
                for j in range(len(cellsWithMines)):
                    if checkForDuplicates and cellsWithMines[i] == cellsWithMines[j] and i != j:
                        cellsWithMines.pop(j)
                        counter -= 1
                        checkForDuplicates = False
        counter += 1

    return cellsWithMines

def cellsCoordinates(rows, columns):
    '''
    This function will create a dictionary that will contain every coordinate of each cell.
    The keys of the dictionary are the number of each row, which were assigned in start.py.
    The values are a list containing the "?" symbol.
    The number of "?"s is equivalent to the number of columns assigned in start.py.
    Since the lists' index number 0 won't be used, it will be assigned with "N/A".
    This function will return said dictionary with the cells' coordinates.
    '''
    rowsNcolumns = {}

    for i in range(1, rows + 1):
        rowsNcolumns[i] = []
        
        for j in range(columns + 1):
            if j != 0:
                rowsNcolumns[i].append("?")
            else:
                rowsNcolumns[i].append("N/A")

    return rowsNcolumns

def showCells(points, totalPoints, flags, moves, rowsNcolumns, columns):
    '''
    This function will print the rowsNcolumns dictionary, each element in one line.

    First, it will print the numbers at the top, the number of each column.
    If there are more than 10 columns, if the column number is lesser or equal than 9, it will also print two blank spaces next to it.
    If there are more than 10 columns, if the column number is greater than 9, it will also print one blank space next to it.
    If there are 10 columns or less, it will always print one blank space next to each number.

    Next, it will print the numbers on the left, the number of each row.
    If the row number is lesser or equal than 9, it will also print three blank spaces next to it.
    If the row number is greater than 9, it will also print two blank spaces next to it.

    Finally, it will print the cells of each row.
    If there are more than 10 columns, it will also print two blank spaces next to each number.
    If there are 10 columns or less, it will also print one blank space next to each number.
    '''
    print(f"\n\nPoints: {points} / {totalPoints}\nFlags: {flags}\nMoves: {moves}\n")

    print("    ", end = "")
    for i in range(1, columns + 1):
        if columns > 10:
            if i > 9:
                print(i, end = " ")
            else:
                print(i, end = "  ")
        else:
            print(i, end = " ")
    print("\n")

    for i in rowsNcolumns.keys():
        if i > 9:
            print(i, end = "  ")
        else:
            print(i, end = "   ")

        for j in range(1, columns + 1):
            if columns > 10:
                print(rowsNcolumns[i][j], end = "  ")
            else:
                print(rowsNcolumns[i][j], end = " ")

        print("")
    print("")

def checkMinesAround(rowLeft, rowRight, columnLeft, columnRight, minesCells, minesAround):
    '''
    This 
    '''
    for i in range(rowLeft, rowRight):
        for j in range(columnLeft, columnRight):
            if [i, j] in minesCells:
                minesAround += 1
                
    return minesAround

def showMines(minesCells, rows):
    '''
    
    '''
    for i in minesCells:
        rows[i[0]][i[1]] = "M"

def checkMinesAroundPreamble(rowChosen, columnChosen, rows, columns, minesCells):
    '''
    
    '''
    minesAround = 0

    if rowChosen != 1 and columnChosen != 1 and rowChosen != rows and columnChosen != columns:
        minesAround = checkMinesAround(rowChosen - 1, rowChosen + 2, columnChosen - 1, columnChosen + 2, minesCells, minesAround)
                    
    elif rowChosen == 1 and columnChosen != 1:
        minesAround = checkMinesAround(rowChosen, rowChosen + 2, columnChosen - 1, columnChosen + 2, minesCells, minesAround)

    elif rowChosen != 1 and columnChosen == 1:
        minesAround = checkMinesAround(rowChosen - 1, rowChosen + 2, columnChosen, columnChosen + 2, minesCells, minesAround)

    elif rowChosen == 1 and columnChosen == 1:
        minesAround = checkMinesAround(rowChosen, rowChosen + 2, columnChosen, columnChosen + 2, minesCells, minesAround)

    elif rowChosen == rows and columnChosen != columns:
        minesAround = checkMinesAround(rowChosen - 1, rowChosen + 1, columnChosen - 1, columnChosen + 2, minesCells, minesAround)

    elif rowChosen != rows and columnChosen == columns:
        minesAround = checkMinesAround(rowChosen - 1, rowChosen + 2, columnChosen - 1, columnChosen + 1, minesCells, minesAround)

    elif rowChosen == rows and columnChosen == columns:
        minesAround = checkMinesAround(rowChosen - 1, rowChosen + 1, columnChosen - 1, columnChosen + 1, minesCells, minesAround)

    return minesAround

def checkMoves(points, flags, moves, lastPlay):
    '''
    
    '''
    if lastPlay[0] != points or lastPlay[1] != flags:
        lastPlay.extend([points, flags])
        lastPlay.pop(0)
        lastPlay.pop(0)
        return moves + 1
    else:
        return moves