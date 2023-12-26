"""
Advent of Code 2023 - Day 14, Part 2

Task: 2048 with stone (do 10000 cycles, each cycle consists of tilting to the first north, then west, then south, then east) and calculate torque.
"""

import numpy as np

def tilt_to_direction(grid, direction):
    """
    Tilt the grid in the specified direction (north, west, south, east).
    """
    if direction == 'north':
        for col in range(len(grid[0])):
            rejoined = []
            for parts in "".join(grid[:, col]).split("#"):
                rejoined.extend(["O"] * parts.count("O") + ["."] * parts.count("."))
                rejoined.append("#")
            del rejoined[-1]
            grid[:, col] = rejoined

    elif direction == 'west':
        for row in range(len(grid)):
            rejoined = []
            for parts in "".join(grid[row]).split("#"):
                rejoined.extend(["O"] * parts.count("O") + ["."] * parts.count("."))
                rejoined.append("#")
            del rejoined[-1]
            grid[row] = rejoined

    elif direction == 'south':
        for col in range(len(grid[0])):
            rejoined = []
            for parts in "".join(grid[:, col]).split("#"):
                rejoined.extend(["."] * parts.count(".") + ["O"] * parts.count("O"))
                rejoined.append("#")
            del rejoined[-1]
            grid[:, col] = rejoined

    elif direction == 'east':
        for row in range(len(grid)):
            rejoined = []
            for parts in "".join(grid[row]).split("#"):
                rejoined.extend(["."] * parts.count(".") + ["O"] * parts.count("O"))
                rejoined.append("#")
            del rejoined[-1]
            grid[row] = rejoined

def cycle(grid):
    """
    Perform a full cycle on the grid.
    """
    tilt_to_direction(grid, 'north')
    tilt_to_direction(grid, 'west')
    tilt_to_direction(grid, 'south')
    tilt_to_direction(grid, 'east')

def calculate_torque_after_cycles(file_path: str) -> int:
    """
    Calculate torque after performing 10000 cycles on the grid.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - int: The sum of torque.
    """
    str_to_cycle = {}
    CYCLES_TO_RUN = int(1e9)

    with open(file_path, "r", encoding="utf8") as file:
        grid = [list(line.strip()) for line in file]

    grid = np.array(grid)

    for iteration in range(CYCLES_TO_RUN):
        cycle(grid)
        grid_repr = tuple(grid.flatten())

        if grid_repr in str_to_cycle:
            first_repeat = iteration
            first_to_be_repeated = str_to_cycle[grid_repr]
            equiv_cycles = first_to_be_repeated + ((CYCLES_TO_RUN - first_to_be_repeated) % (first_repeat - first_to_be_repeated)) - 1
            grid = np.array(str_to_cycle[equiv_cycles]).reshape((len(grid), len(grid[0])))
            break

        str_to_cycle[grid_repr] = iteration
        str_to_cycle[iteration] = grid_repr

    torque = sum((len(grid) - i) * np.sum(grid[i] == "O") for i in range(len(grid)))
    return torque

if __name__ == "__main__":
    input_file_path = "input.txt"
    result = calculate_torque_after_cycles(input_file_path)
    print(f"The sum of torque is: {result}")
