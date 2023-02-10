from functions import *

def minesweeper(rows, columns, mines):
    '''
    The main function of the program.
    Check functions.py for a detailed explanation of each function used in this module.
    '''
    cellsWithMines = minesCoordinates(rows, columns, mines)
    cells = cellsCoordinates(rows, columns)

    points = 0
    totalPoints = (rows * columns) - mines
    flags = mines
    moves = 0
    lastMove = [points, flags]
    selectedCells = []
    
    playing = True

    while playing:
        showCells(points, totalPoints, flags, moves, cells, columns)
        print("1. Cell\n2. Flag\n")
        choice = input("Select (1/2): ")

        match choice:
            case "1":
                cellChosen = input("Select cell: ")
                try:
                    rowChosen = int(cellChosen.split(",")[0].strip())
                    columnChosen = int(cellChosen.split(",")[1].strip())
                except (ValueError, IndexError):
                    rowChosen = 0
                    columnChosen = 0

                if [rowChosen, columnChosen] in cellsWithMines and cells[rowChosen][columnChosen] != "F":
                    playing = False
                    moves += 1
                    showMines(cellsWithMines, cells)
                    showCells(points, totalPoints, flags, moves, cells, columns)
                    print("You lost!")

                elif rowChosen > 0 and rowChosen <= rows and columnChosen > 0 and columnChosen <= columns \
                and cells[rowChosen][columnChosen] != "F" and [rowChosen, columnChosen] not in selectedCells:

                    selectedCellMinesAround = checkMinesAround(rowChosen, columnChosen, rows, columns, cellsWithMines)
                    cells[rowChosen][columnChosen] = selectedCellMinesAround
                    selectedCells.append([rowChosen, columnChosen])
                    points += 1

                    points = checkCellsAround(rowChosen, columnChosen, rows, columns, selectedCells, cellsWithMines, cells, selectedCellMinesAround, points)

                if points == totalPoints:
                    playing = False
                    moves += 1
                    showMines(cellsWithMines, cells)
                    showCells(points, totalPoints, flags, moves, cells, columns)
                    print("You win!")

            case "2":
                cellChosen = input("Select cell: ")
                try:
                    rowChosen = int(cellChosen.split(",")[0].strip())
                    columnChosen = int(cellChosen.split(",")[1].strip())
                except (ValueError, IndexError):
                    rowChosen = 0
                    columnChosen = 0

                flags = addFlag(rowChosen, rows, columnChosen, columns, cells, flags, mines)

            case _:
                pass
        
        moves = checkMoves(points, flags, moves, lastMove)