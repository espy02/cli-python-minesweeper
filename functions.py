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
    This function will create a dictionary that will contain the coordinates of each cell.
    The keys of the dictionary are the number of each row, which were assigned in start.py.
    The values are a list containing the "?" symbol.
    The number of "?"s is equivalent to the number of columns assigned in start.py.
    Since the lists' index number 0 won't be used, it will be assigned with "N/A".
    This function will return said dictionary with the cells' coordinates.
    '''
    cells = {}

    for i in range(1, rows + 1):
        cells[i] = []
        
        for j in range(columns + 1):
            if j != 0:
                cells[i].append("?")
            else:
                cells[i].append("N/A")

    return cells

def showCells(points, totalPoints, flags, moves, cells, columns):
    '''
    This function will print the cells dictionary, each element in one line.

    First, it will print the numbers at the top, the number of each column.
    If there are more than 10 columns, if the column number is lesser or equal than 9, print two blank spaces next to the number.
    If there are more than 10 columns, if the column number is greater than 9, print one blank space next to the number.
    If there are 10 columns or less, print one blank space next to each number.

    Next, it will print the numbers on the left, the number of each row.
    If the row number is lesser or equal than 9, print three blank spaces next to the number.
    If the row number is greater than 9, print two blank spaces next to the number.

    Finally, it will print the cells of each row.
    If there are more than 10 columns, print two blank spaces next to each number.
    If there are 10 columns or less, print one blank space next to each number.
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

    for i in cells.keys():
        if i > 9:
            print(i, end = "  ")
        else:
            print(i, end = "   ")

        for j in range(1, columns + 1):
            if columns > 10:
                print(cells[i][j], end = "  ")
            else:
                print(cells[i][j], end = " ")

        print("")
    print("")

def checkMoves(points, flags, moves, lastPlay):
    '''
    This function will check if the user has made a move.
    A user has made a move if the number of points or the number of flags has changed since the last play.
    The lastPlay list contains the number of points and the number of flags of the last play.
    This function will return the number of moves.
    '''
    if lastPlay[0] != points or lastPlay[1] != flags:
        lastPlay.extend([points, flags])
        lastPlay.pop(0)
        lastPlay.pop(0)
        return moves + 1
    else:
        return moves

def showMines(cellsWithMines, cells):
    '''
    This function will change every cell with a mine in the cells dictionary to the character "M".
    This function is called when the user loses the game or wins the game.
    '''
    for i in cellsWithMines:
        cells[i[0]][i[1]] = "M"

def checkMinesAround(rowChosen, columnChosen, rows, columns, cellsWithMines):
    '''
    
    '''
    minesAround = 0
    rowLeft = rowChosen - 1
    rowRight = rowChosen + 2
    columnLeft = columnChosen - 1
    columnRight = columnChosen + 2
      
    if rowChosen == 1 and columnChosen != 1:
        rowLeft = rowChosen

    elif rowChosen != 1 and columnChosen == 1:
        columnLeft = columnChosen

    elif rowChosen == 1 and columnChosen == 1:
        rowLeft = rowChosen
        columnLeft = columnChosen

    elif rowChosen == rows and columnChosen != columns:
        rowRight = rowChosen + 1

    elif rowChosen != rows and columnChosen == columns:
        columnRight = columnChosen + 1

    elif rowChosen == rows and columnChosen == columns:
        rowRight = rowChosen + 1
        columnRight = columnChosen + 1

    for i in range(rowLeft, rowRight):
        for j in range(columnLeft, columnRight):
            if [i, j] in cellsWithMines:
                minesAround += 1

    return minesAround

def checkCellsAround(rowChosen, columnChosen, rows, columns, cellsSelected, cellsWithMines, cells, selectedCellMinesAround, points):
    '''
    This function will check if the cell above, below, to the right, and to the left of the selected cell has the same number of mines around it.
    Those cells will be added to cellsAround.
    The cells that have the same number of mines around as the selected cell will be automatically selected and added to cellsSelected.
    Then, just like the original selected cell, the cell above, below, to the right, and to the left of a cell added to cellsSelected,
    will also be added to cellsAround.
    Once a cell is verified, it will be removed from cellsAround*.
    If the cell is in cellsSelected, or is a cell with a mine, or is a cell with a flag, or has a 0 on its coordinates,
    or has a coordinate that is greater than the respective number of rows or number of columns, 
    then it will not be verified and it will be removed from cellsAround.
    *(except the original selected cell, since it was never in the list to begin with)
    '''
    cellsAround = [[rowChosen - 1, columnChosen], [rowChosen, columnChosen - 1], [rowChosen, columnChosen + 1], \
    [rowChosen + 1, columnChosen]]

    while len(cellsAround) != 0:
        if cellsAround[0][0] > 0 and cellsAround[0][0] <= rows and cellsAround[0][1] > 0 and cellsAround[0][1] <= columns \
        and [cellsAround[0][0], cellsAround[0][1]] not in cellsSelected and [cellsAround[0][0], cellsAround[0][1]] not in cellsWithMines \
        and cells[cellsAround[0][0]][cellsAround[0][1] - 1] != "F" \
        and checkMinesAround(cellsAround[0][0], cellsAround[0][1], rows, columns, cellsWithMines) == selectedCellMinesAround:
            cells[cellsAround[0][0]][cellsAround[0][1]] = selectedCellMinesAround
            cellsSelected.append([cellsAround[0][0], cellsAround[0][1]])
            points += 1
            cellsAround.extend([[cellsAround[0][0] - 1, cellsAround[0][1]],  [cellsAround[0][0], cellsAround[0][1] - 1], \
            [cellsAround[0][0], cellsAround[0][1] + 1], [cellsAround[0][0] + 1, cellsAround[0][1]]])
        cellsAround.pop(0)

    return points