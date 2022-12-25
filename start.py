from game import minesweeper

playing = True

while playing:
    restart = ""

    print("Python Minesweeper by espy02.\nhttps://github.com/espy02/python-minesweeper\n")
    print("Select the difficulty:\n\n1. Beginner - 10x10 / 10 mines\n2. Intermediate - 16x16 / 40 mines\n3. Expert - 30x16 / 99 mines\n4. Custom\n")
    diff = input("Difficulty (1/2/3/4): ")

    match diff:
        case "1":
            rows = 10
            columns = 10
            mines = 10
            minesweeper(rows, columns, mines)

        case "2":
            rows = 16
            columns = 16
            mines = 40
            minesweeper(rows, columns, mines)

        case "3":
            rows = 30
            columns = 16
            mines = 99
            minesweeper(rows, columns, mines)

        case "4":
            rows = int(input("Rows: "))
            columns = int(input("Columns: "))
            mines = int(input("Mines: "))

            if rows == 0 or columns == 0:
                print("\nNot enough rows/columns!\n")
                restart = "y"

            elif mines > (rows * columns):
                print("\nToo many bombs!\n")
                restart = "y"

            else:
                minesweeper(rows, columns, mines)

        case _:
            print("")
            restart = "y"

    while restart != "y" and restart != "n":
        restart = input("Do you want to restart? (y/n): ")
        match restart:
            case "n":
                playing = False
            case _:
                pass
