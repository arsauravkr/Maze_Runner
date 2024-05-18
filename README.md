# Maze Runner

A fun and engaging maze-solving game implemented in Python. Help the rabbit find its way to the carrot through a randomly generated maze.

## Problem Statement

Create a Python-based maze-solving game where a rabbit must find its way to a carrot. The game uses a user-defined grid size where `0` represents a path and `X` represents a blocked cell. The maze is randomly generated each time the game is run with a fixed probability of 0.3 for blocked cells. The rabbit starts at the top-left corner (`R`) and aims to reach the bottom-right corner (`C`) where the carrot is located. The program should find a path if it exists and print the solution step-by-step. The game allows the user to replay multiple times.

## Logic

1. **Random Maze Generation**:
    - Generate a random maze with a fixed block probability of 0.3.
    - Ensure that the start and end points are not blocked.

2. **Recursive Function**:
    - Define a recursive function `solve_maze` that tries to find a path from the current cell to the carrot.
    - Base Case: If the current cell is the destination, mark it and return `True`.
    - Check if the current cell is valid (within bounds, a path, and not already part of the solution).
    - Mark the current cell as part of the solution and print the current state.
    - Recursively attempt to move in four possible directions: down, right, up, and left.
    - If a move is successful, return `True`.
    - If none of the moves work, backtrack by unmarking the current cell and print the state.
    - Return `False` if no path is found.

3. **Execution**:
    - Get user input for maze size.
    - Generate the random maze and initialize the solution matrix.
    - Print the randomly generated maze with 'R' for the rabbit and 'C' for the carrot.
    - Call `solve_maze` starting from the top-left corner.
    - Print the final solution or a failure message.
    - Ask the user if they want to play again.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/arsauravkr/Maze_Runner.git
    cd Maze_Runner
    ```

2. Run the game:
    ```bash
    python maze_runner.py
    ```

## How to Play

- The game will prompt you to enter the size of the maze.
- The randomly generated maze and the current state of the solution at each step will be displayed.
- If a path is found, the final solution will be displayed.
- If no path exists, a failure message will be shown.
- After each game, you will be asked if you want to play again.

## Example

```plaintext
Enter the size of the maze (e.g., 5 for a 5x5 maze): 5
Maze:
R _ X _ _
X _ _ X _
_ _ _ _ _
X X X X _
X _ _ _ C
====================
Solution:
O O X _ _
X O O X _
_ _ O O O
X X X X O
X _ _ _ O
--------------------
Hooray! The rabbit found the carrot!
