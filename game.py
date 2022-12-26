from functions import *

def minesweeper(rows, columns, mines):
    cellsWithMines = minesCoordinates(rows, columns, mines)

    rowsNcolumns = cellsCoordinates(rows, columns)

    points = 0
    totalPoints = (rows * columns) - mines
    flags = mines
    moves = 0
    cellsSelected = []
    lastPlay = [points, flags]
    playing = True

    while playing:
        showCells(points, totalPoints, flags, moves, rowsNcolumns, columns)
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

                if [rowChosen, columnChosen] in cellsWithMines and rowsNcolumns[rowChosen][columnChosen] != "F":
                    playing = False
                    showMines(cellsWithMines, rowsNcolumns)
                    moves = checkMoves(points, flags, moves, lastPlay)
                    showCells(points, totalPoints, flags, moves, rowsNcolumns, columns)
                    print("You lost!")

                elif rowChosen > 0 and rowChosen <= rows and columnChosen > 0 and columnChosen <= columns \
                and rowsNcolumns[rowChosen][columnChosen] != "F" and [rowChosen, columnChosen] not in cellsSelected:
                    minesAround = checkMinesAroundPreamble(rowChosen, columnChosen, rows, columns, cellsWithMines)
                    rowsNcolumns[rowChosen][columnChosen] = minesAround
                    playedCellMinesAround = minesAround
                    cellsSelected.append([rowChosen, columnChosen])
                    points += 1

                    cellsAround = [[rowChosen - 1, columnChosen], [rowChosen, columnChosen - 1], [rowChosen, columnChosen + 1], \
                    [rowChosen + 1, columnChosen]]

                    for i in range(3):
                        checkCellsAround = 0
                        while checkCellsAround != 3:
                            if checkCellsAround < len(cellsAround):
                                if cellsAround[checkCellsAround][0] <= 0 or cellsAround[checkCellsAround][0] > rows \
                                or cellsAround[checkCellsAround][1] <= 0 or cellsAround[checkCellsAround][1] > columns:
                                    cellsAround.remove([cellsAround[checkCellsAround][0], cellsAround[checkCellsAround][1]])
                            checkCellsAround += 1

                    while len(cellsAround) != 0:
                        if cellsAround[0][0] > 0 and cellsAround[0][0] <= rows \
                        and cellsAround[0][1] > 0 and cellsAround[0][1] <= columns \
                        and [cellsAround[0][0], cellsAround[0][1]] not in cellsSelected \
                        and [cellsAround[0][0], cellsAround[0][1]] not in cellsWithMines \
                        and rowsNcolumns[cellsAround[0][0]][cellsAround[0][1] - 1] != "F":
                            if checkMinesAroundPreamble(cellsAround[0][0], cellsAround[0][1], rows, columns, cellsWithMines) \
                            == playedCellMinesAround:
                                rowsNcolumns[cellsAround[0][0]][cellsAround[0][1]] = playedCellMinesAround
                                cellsSelected.append([cellsAround[0][0], cellsAround[0][1]])
                                points += 1
                                cellsAround.extend([[cellsAround[0][0] - 1, cellsAround[0][1]],  [cellsAround[0][0], cellsAround[0][1] - 1], \
                                [cellsAround[0][0], cellsAround[0][1] + 1], [cellsAround[0][0] + 1, cellsAround[0][1]]])
                        cellsAround.pop(0)

                if points == totalPoints:
                    playing = False
                    showMines(cellsWithMines, rowsNcolumns)
                    moves = checkMoves(points, flags, moves, lastPlay)
                    showCells(points, totalPoints, flags, moves, rowsNcolumns, columns)
                    print("You win!")

            case "2":
                try:
                    rowChosen = int(input("Row: "))
                    columnChosen = int(input("Column: "))
                except ValueError:
                    rowChosen = 0
                    columnChosen = 0

                if rowChosen > 0 and rowChosen <= rows and columnChosen > 0 and columnChosen <= columns:
                    if rowsNcolumns[rowChosen][columnChosen] == "?" and flags > 0:
                        rowsNcolumns[rowChosen - 1][columnChosen] = "F"
                        flags -= 1
                    elif rowsNcolumns[rowChosen][columnChosen] == "F" and flags < mines:
                        rowsNcolumns[rowChosen][columnChosen] = "?"
                        flags += 1

            case _:
                pass
        
        moves = checkMoves(points, flags, moves, lastPlay)