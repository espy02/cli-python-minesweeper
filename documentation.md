WIP

# start.py
## Variables
`playing` - Boolean variable that will remain `True` until the user chooses not to restart after finishing a game.

`restart` - String variable used to chose whether the user wants to replay or not.

`diff` - String variable used to choose which difficulty to play.

`rows`- Integer variable. The number of rows. Can be either one of the three default values or one entered by the user.

`columns`- The number of columns. Can be either one of the three default values or one entered by the user.

`mines` - The number of mines. Can be either one of the three default values or one entered by the user.

# Coomprehensive explanation

`playing` is assigned with `True`, to allow the program to keep running, even if the user enters an unnessary value to either `restart` or `diff`. Once the program starts, the user can choose one of four values to assign to `diff`. The first three options will assign their respective default values to `rows`, `columns` and `mines`, while the fourth option will allow the user to choose how many rows, columns and mines they want in the game. If this option is selected, neither `rows` or `columns` can be assigned with `0`, and the number of bombs can't exceed the number of cells. When they finish a game, the user can choose if they want to restart, by entering `"y"` or `"n"` to `restart`.
