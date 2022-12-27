from game import minesweeper

playing = True

while playing:
    restart = ""

    print("\nPython Minesweeper by espy02, v1.1\nhttps://github.com/espy02/python-minesweeper\n")
    print("Select the difficulty:\n\n1. Beginner - 10x10 / 10 mines\n2. Intermediate - 16x16 / 40 mines\n3. Expert - 30x16 / 99 mines\n4. Custom\n")
    difficulty = input("Difficulty (1/2/3/4): ")

    match difficulty:
        case "1":
            input("\nNote: to select a cell, enter the number of the row, and the number of the column, separated by a comma.\nExample: 4,5\nPress enter to continue.")
            minesweeper(rows = 10, columns = 10, mines = 10)

        case "2":
            input("\nNote: to select a cell, enter the number of the row, and the number of the column, separated by a comma.\nExample: 4,5\nPress enter to continue.")
            minesweeper(rows = 16, columns = 16, mines = 40)

        case "3":
            input("\nNote: to select a cell, enter the number of the row, and the number of the column, separated by a comma.\nExample: 4,5\nPress enter to continue.")
            minesweeper(rows = 30, columns = 16, mines = 99)

        case "4":
            try:
                rows = int(input("Rows: "))
                columns = int(input("Columns: "))
                mines = int(input("Mines: "))
            except ValueError:
                rows = 0
                columns = 0
                mines = 0

            if rows == 0 or columns == 0:
                print("\nNot enough rows/columns!")
                restart = "y"

            elif mines > (rows * columns):
                print("\nToo many bombs!")
                restart = "y"

            else:
                input("\nNote: to select a cell, enter the number of the row, and the number of the column, separated by a comma.\nExample: 4,5\nPress enter to continue.")
                minesweeper(rows, columns, mines)

        case _:
            restart = "y"

    while restart != "y" and restart != "n":
        restart = input("Do you want to restart? (y/n): ")
        match restart:
            case "n":
                playing = False
            case _:
                pass