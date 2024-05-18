import random

def generate_random_maze(size, block_probability=0.3):
    """Generates a random maze with given size and block probability."""
    maze = [[0 if random.random() > block_probability else 1 for _ in range(size)] for _ in range(size)]
    maze[0][0] = 0  # Ensure the start is not blocked
    maze[size-1][size-1] = 0  # Ensure the end is not blocked
    return maze

def print_maze(maze):
    """Prints the maze with 'X' for blocked cells and '_' for open paths."""
    print("Maze:")
    size = len(maze)
    for r in range(size):
        row = []
        for c in range(size):
            if r == 0 and c == 0:
                row.append('R')  # Mark the start with 'R' for Rabbit
            elif r == size-1 and c == size-1:
                row.append('C')  # Mark the end with 'C' for Carrot
            else:
                row.append('X' if maze[r][c] else '_')
        print(" ".join(row))
    print("=" * 11)

def print_solution(maze, solution):
    """Prints the current solution matrix with 'O' for the path and 'X' for blocked cells."""
    size = len(maze)
    print("Solution:")
    for r in range(size):
        row = []
        for c in range(size):
            if maze[r][c] == 1:
                row.append('X')
            elif solution[r][c] == 1:
                row.append('O')
            else:
                row.append('_')
        print(" ".join(row))
    print("-" * 11)

def solve_maze(maze, solution, size, r, c):
    """Recursively attempts to solve the maze."""
    if r == size - 1 and c == size - 1:  # If the destination (carrot) is reached
        solution[r][c] = 1
        return True

    if 0 <= r < size and 0 <= c < size and maze[r][c] == 0 and solution[r][c] == 0:
        solution[r][c] = 1  # Mark the current cell as part of the solution
        print_solution(maze, solution)

        # Try moving in all four possible directions
        if solve_maze(maze, solution, size, r + 1, c):  # Move down
            return True
        if solve_maze(maze, solution, size, r, c + 1):  # Move right
            return True
        if solve_maze(maze, solution, size, r - 1, c):  # Move up
            return True
        if solve_maze(maze, solution, size, r, c - 1):  # Move left
            return True

        solution[r][c] = 0  # If none of the above moves work, backtrack
        print_solution(maze, solution)
        return False

    return False

def main():
    """Main function to run the maze solver."""
    while True:
        try:
            size = int(input("Enter the size of the maze (e.g., 5 for a 5x5 maze): "))
        except ValueError:
            print("Invalid input. Please enter a valid number for size.")
            continue

        maze = generate_random_maze(size)
        solution = [[0] * size for _ in range(size)]

        print_maze(maze)

        if solve_maze(maze, solution, size, 0, 0):
            print("Hooray! The rabbit found the carrot!")
            print_solution(maze, solution)
        else:
            print("Oh no! The rabbit couldn't find the carrot.")
            print_solution(maze, solution)

        replay = input("Do you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()