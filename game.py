from random import randint
from functions import *

def game(rows, columns, mines):
    minesCells = {}
    minesNumber = 0

    while minesNumber < mines:
        minesCells[minesNumber] = [randint(1, rows), randint(1, columns)]
        duplicateCheck = True
    
        if len(minesCells) > 1:
            for i in range(len(minesCells)):
                for j in range(len(minesCells)):
                    if duplicateCheck:
                        if minesCells[i] == minesCells[j] and i != j:
                            minesCells.pop(j)
                            minesNumber -= 1
                            duplicateCheck = False
        minesNumber += 1

    rowsNcolumns = {}

    for i in range(rows):
        rowsNcolumns[i] = []

    for i in rowsNcolumns.values():
        for j in range(columns):
            i.append("?")

    points = 0
    flags = minesNumber
    cellsChecked = []
    playing = True

    while playing:
        print("\nPoints:", points, "/", (rows * columns) - mines, "\nFlags:", flags)
        showCells(rowsNcolumns, columns)
        print("1. Cell\n2. Flag\n")
        choice = input("Select (1/2): ")

        match choice:

            case "1":
                try:
                    rowChosen = int(input("Row: "))
                    columnChosen = int(input("Column: "))
                except ValueError:
                    rowChosen = 0
                    columnChosen = 0

                if [rowChosen, columnChosen] in minesCells.values() and rowsNcolumns[rowChosen - 1][columnChosen - 1] != "F":
                    playing = False
                    showMines(minesCells, rowsNcolumns)
                    print("\nPoints:", points, "/", (rows * columns) - mines, "\nFlags:", flags)
                    showCells(rowsNcolumns, columns)
                    print("You lost!")

                elif rowChosen > 0 and rowChosen <= rows and columnChosen > 0 and columnChosen <= columns \
                and rowsNcolumns[rowChosen - 1][columnChosen - 1] != "F":
                    
                    minesAround = checkMinesAroundPreamble(rowChosen, columnChosen, rows, columns, minesCells)

                    rowsNcolumns[rowChosen - 1][columnChosen - 1] = minesAround

                    playedCellMinesNumber = minesAround

                    if [rowChosen - 1, columnChosen - 1] not in cellsChecked:
                        cellsChecked.append([rowChosen - 1, columnChosen - 1])
                        points += 1

                        cellsAround = [[rowChosen - 1, columnChosen - 1], [rowChosen - 1, columnChosen], [rowChosen - 1, columnChosen + 1], \
                        [rowChosen, columnChosen - 1], [rowChosen, columnChosen + 1], \
                        [rowChosen + 1, columnChosen - 1], [rowChosen + 1, columnChosen], [rowChosen + 1, columnChosen + 1]]


                        for i in range(len(cellsAround)):
                            checkCellsAround = 0
                            while checkCellsAround != 7:
                                if checkCellsAround < len(cellsAround):
                                    if cellsAround[checkCellsAround][0] <= 0 or cellsAround[checkCellsAround][0] > rows \
                                    or cellsAround[checkCellsAround][1] <= 0 or cellsAround[checkCellsAround][1] > columns:
                                        cellsAround.remove([cellsAround[checkCellsAround][0], cellsAround[checkCellsAround][1]])
                                checkCellsAround += 1

                        while len(cellsAround) != 0:
                            if cellsAround[0][0] > 0 and cellsAround[0][0] <= rows \
                            and cellsAround[0][1] > 0 and cellsAround[0][1] <= columns \
                            and [cellsAround[0][0] - 1, cellsAround[0][1] - 1] not in cellsChecked \
                            and [cellsAround[0][0], cellsAround[0][1]] not in minesCells.values() \
                            and rowsNcolumns[cellsAround[0][0] - 1][cellsAround[0][1] - 1] != "F":
                                if checkMinesAroundPreamble(cellsAround[0][0], cellsAround[0][1], rows, columns, minesCells) \
                                    == playedCellMinesNumber:
                                    rowsNcolumns[cellsAround[0][0] - 1][cellsAround[0][1] - 1] = playedCellMinesNumber
                                    cellsChecked.append([cellsAround[0][0] - 1, cellsAround[0][1] - 1])
                                    points += 1
                                    cellsAround.extend([[cellsAround[0][0] - 1, cellsAround[0][1] - 1], [cellsAround[0][0] - 1, cellsAround[0][1]], [cellsAround[0][0] - 1, cellsAround[0][1] + 1], \
                                    [cellsAround[0][0], cellsAround[0][1] - 1], [cellsAround[0][0], cellsAround[0][1] + 1], \
                                    [cellsAround[0][0] + 1, cellsAround[0][1] - 1], [cellsAround[0][0] + 1, cellsAround[0][1]], [cellsAround[0][0] + 1, cellsAround[0][1] + 1]])
                            cellsAround.pop(0)

                    if points == (rows * columns) - mines:
                        playing = False
                        showMines(minesCells, rowsNcolumns)
                        print("\nPoints:", points, "/", (rows * columns) - mines, "\nFlags:", flags)
                        showCells(rowsNcolumns, columns)
                        print("You win!")

            case "2":
                try:
                    rowChosen = int(input("Row: "))
                    columnChosen = int(input("Column: "))
                except ValueError:
                    rowChosen = 0
                    columnChosen = 0

                if rowChosen > 0 and rowChosen <= rows and columnChosen > 0 and columnChosen <= columns:
                    if rowsNcolumns[rowChosen - 1][columnChosen - 1] == "?" and flags > 0:
                        rowsNcolumns[rowChosen - 1][columnChosen - 1] = "F"
                        flags -= 1
                    elif rowsNcolumns[rowChosen - 1][columnChosen - 1] == "F" and flags < minesNumber:
                        rowsNcolumns[rowChosen - 1][columnChosen - 1] = "?"
                        flags += 1

            case _:
                pass
