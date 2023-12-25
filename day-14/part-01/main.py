"""
Advent of Code 2023 - Day 14, Part 1

Task: 2048 with stone  and calculate torque.
"""
import numpy as np

def calculate_torque_after_roll(file_path: str) -> int:
    """
    Calculate torque after the roll based on the stone positions in the grid.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - int: The sum of torque.
    """

    # Read the grid from the file
    with open(file_path, "r", encoding="utf8") as file:
        grid = [list(line.strip()) for line in file]

    grid = np.array(grid)

    # Process each column in the grid
    for col in range(len(grid[0])):
        rejoined = []

        # Split the column by "#" and rebuild it with "O" and "."
        for parts in "".join(grid[:, col]).split("#"):
            rejoined.extend(["O"] * parts.count("O") + ["."] * parts.count("."))
            rejoined.append("#")

        del rejoined[-1]
        grid[:, col] = rejoined

    torque = 0 
    ROWS = len(grid)

    # Calculate torque for each row
    for i in range(ROWS):
        torque += sum(grid[i] == "O") * (ROWS - i)

    return torque

if __name__ == "__main__":
    input_file_path = "input.txt"
    result = calculate_torque_after_roll(input_file_path)
    print(f"The sum of torque is: {result}")
