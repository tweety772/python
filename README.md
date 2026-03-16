# Tic-Tac-Toe in Python

This is a simple console-based Tic-Tac-Toe game I wrote in Python. 

## How it works
- The game is played on a basic 3x3 grid.
- The computer plays as 'X' and always makes the first move in the middle (square 5).
- The player plays as 'O'.
- You simply pick a number from 1 to 9 to make your move.
- The computer doesn't use a complex AI; it just picks a random available square using `randrange()`.

## Code Structure
I organized the logic into a few main functions to keep the code clean:
- `display_board()`: Prints the current state of the grid.
- `enter_move()`: Takes the user's input and ensures it's a valid move.
- `make_list_of_free_fields()`: Checks the board for empty spots.
- `victory_for()`: Checks the rows, columns, and diagonals to see if someone won.
- `draw_move()`: Handles the computer's random turn.

## How to run
Just download the python file and run it in your terminal:

```bash
python main.py
