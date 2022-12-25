def showCells(rowsNcolumns, columns):
    print("\n   ", end = " ")

    for i in range(columns):
        if columns > 10:
            if i > 8:
                print(i + 1, end = " ")
            else:
                print(i + 1, end = "  ")
        else:
            print(i + 1, end = " ")

    print("")
    print("")

    for i in rowsNcolumns.keys():

        if i + 1 < 10:
            print(i + 1, end = "   ")
        else:
            print(i + 1, end = "  ")

        for j in range(columns):
            if columns > 10:
                print(rowsNcolumns[i][j], end = "  ")
            else:
                print(rowsNcolumns[i][j], end = " ")

        print("")
    print("")

def checkMinesAround(rowLeft, rowRight, columnLeft, columnRight, minesCells, minesAround):
    for i in range(rowLeft, rowRight):
        for j in range(columnLeft, columnRight):
            if [i, j] in minesCells:
                minesAround += 1
                
    return minesAround

def showMines(minesCells, rows):
    for i in minesCells:
        rows[i[0] - 1][i[1] - 1] = "M"

def checkMinesAroundPreamble(rowChosen, columnChosen, rows, columns, minesCells):
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
    if lastPlay[0] != points or lastPlay[1] != flags:
        lastPlay.extend([points, flags])
        lastPlay.pop(0)
        lastPlay.pop(0)
        return moves + 1
    else:
        return moves