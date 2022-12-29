# python-minesweeper
Python Minesweeper is a simple Minesweeper clone that can be played straight through the terminal, using Python 3.11.

## Usage
Simply change your directory inside the terminal to a folder with the following files:

- `start.py`
- `game.py`
- `functions.py`

and execute the program with the command `python start.py`.

![img01](https://i.imgur.com/XBxOh63.png)

You will be prompted to choose a difficulty. The default difficulties are `Beginner`, `Intermediate` and `Expert`, but you can choose the number of rows, columns and mines using the `Custom` difficulty.

![img02](https://i.imgur.com/DeZ9fqV.png)

You can now begin playing. You can select a cell, or place a flag on a cell. 

- You can't select a cell with a flag, but you can remove a flag from a cell by using the `Flag` option again.
- Once you select a cell that does not have a mine, all cells near the chosen cell that have the same number of mines around them will also be automatically selected.
- You win when you select every cell that does not have a mine, and you lose if you select any cell with a mine.

![img03](https://i.ibb.co/ggfwk64/img04.gif)
