from game import game

playing = True

while playing:

    print("Python Minesweeper by espy02.\nhttps://github.com/espy02/python-minesweeper\n")
    print("Select the difficulty:\n\n1. Beginner - 10x10 / 10 mines\n2. Intermediate - 16x16 / 40 mines\n3. Expert - 30x16 / 99 mines\n4. Custom\n")
    diff = input("Difficulty (1/2/3/4): ")

    match diff:
        case "1":
            rows = 10
            columns = 10
            mines = 10
            game(rows, columns, mines)
            playing = False

        case "2":
            rows = 16
            columns = 16
            mines = 40
            game(rows, columns, mines)
            playing = False

        case "3":
            rows = 30
            columns = 16
            mines = 99
            game(rows, columns, mines)
            playing = False

        case "4":
            rows = int(input("Rows: "))
            columns = int(input("Columns: "))
            mines = int(input("Mines: "))

            if mines <= (rows * columns):
                game(rows, columns, mines)
                playing = False
            else:
                print("Too many bombs!\n")
        case _:
            print("")
