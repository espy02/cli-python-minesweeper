from functions import *

def minesweeper(rows, columns, mines):
    cellsWithMines = minesCoordinates(rows, columns, mines)
    
    cells = cellsCoordinates(rows, columns)

    points = 0
    totalPoints = (rows * columns) - mines
    flags = mines
    moves = 0

    cellsSelected = []
    lastPlay = [points, flags]
    playing = True

    while playing:
        showCells(points, totalPoints, flags, moves, cells, columns)
        print("1. Cell\n2. Flag\n")
        choice = input("Select (1/2): ")

        match choice:
            case "1":
                cellChosen = input("Select cell (row, column): ")
                try:
                    rowChosen = int(cellChosen.split(",")[0].strip())
                    columnChosen = int(cellChosen.split(",")[1].strip())
                except (ValueError, IndexError):
                    rowChosen = 0
                    columnChosen = 0

                if [rowChosen, columnChosen] in cellsWithMines and cells[rowChosen][columnChosen] != "F":
                    playing = False
                    moves = checkMoves(points, flags, moves, lastPlay)
                    showMines(cellsWithMines, cells)
                    showCells(points, totalPoints, flags, moves, cells, columns)
                    print("You lost!")

                elif rowChosen > 0 and rowChosen <= rows and columnChosen > 0 and columnChosen <= columns \
                and cells[rowChosen][columnChosen] != "F" and [rowChosen, columnChosen] not in cellsSelected:

                    selectedCellMinesAround = checkMinesAround(rowChosen, columnChosen, rows, columns, cellsWithMines)
                    cells[rowChosen][columnChosen] = selectedCellMinesAround
                    cellsSelected.append([rowChosen, columnChosen])
                    points += 1

                    points = checkCellsAround(rowChosen, columnChosen, rows, columns, cellsSelected, cellsWithMines, cells, selectedCellMinesAround, points)

                if points == totalPoints:
                    playing = False
                    moves = checkMoves(points, flags, moves, lastPlay)
                    showMines(cellsWithMines, cells)
                    showCells(points, totalPoints, flags, moves, cells, columns)
                    print("You win!")

            case "2":
                cellChosen = input("Select cell (row, column): ")
                try:
                    rowChosen = int(cellChosen.split(",")[0].strip())
                    columnChosen = int(cellChosen.split(",")[1].strip())
                except (ValueError, IndexError):
                    rowChosen = 0
                    columnChosen = 0

                if rowChosen > 0 and rowChosen <= rows and columnChosen > 0 and columnChosen <= columns:
                    if cells[rowChosen][columnChosen] == "?" and flags > 0:
                        cells[rowChosen][columnChosen] = "F"
                        flags -= 1
                    elif cells[rowChosen][columnChosen] == "F" and flags < mines:
                        cells[rowChosen][columnChosen] = "?"
                        flags += 1

            case _:
                pass
        
        moves = checkMoves(points, flags, moves, lastPlay)