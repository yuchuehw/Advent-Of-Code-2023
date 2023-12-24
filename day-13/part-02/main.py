"""
Advent of Code 2023 - Day 13, Part 2

Task: First fix symmetry then "summarize" them (sum of vert-symmetry + sum of hori-symmetry * 100)
"""

import time
import numpy as np

def parse_puzzle(file_path: str) -> list:
    """
    Parse the puzzle from the given file and return a list of grids.

    Parameters:
    - file_path (str): Path to the file containing the puzzle.

    Returns:
    - list: A list of 2D grids representing the puzzles.
    """
    with open(file_path, "r", encoding="utf8") as file:
        return [np.array([[{"#": 0, ".": 1}[_] for _ in line.strip()] for line in puzzle.splitlines()]) for puzzle in file.read().split("\n\n")]

def check_symmetry(grid: np.ndarray) -> int:
    """
    Check for symmetry in the given grid and return the sum based on the rules.

    Parameters:
    - grid (np.ndarray): 2D grid representing the puzzle.

    Returns:
    - int: The calculated sum based on symmetry rules.
    """
    sum_ = 0
    height, width = grid.shape

    # Check for vertical symmetry
    for j in range(1, width):
        if np.sum(np.abs(grid[:, j] - grid[:, j - 1])) == 1:
            flag = True
            for a, b in zip(range(j + 1, width), range(j - 2, -1, -1)):
                if not np.array_equal(grid[:, a], grid[:, b]):
                    flag = False
                    break
            if flag:
                sum_ += j
        elif np.sum(np.abs(grid[:, j] - grid[:, j - 1])) == 0:
            diff = 0
            for a, b in zip(range(j + 1, width), range(j - 2, -1, -1)):
                diff += np.sum(np.abs(grid[:, a] - grid[:, b]))
                if diff > 1:
                    break
            if diff == 1:
                sum_ += j

    # Check for horizontal symmetry
    for i in range(1, height):
        if np.sum(np.abs(grid[i] - grid[i - 1])) == 1:
            flag = True
            for a, b in zip(range(i + 1, height), range(i - 2, -1, -1)):
                if not np.array_equal(grid[a], grid[b]):
                    flag = False
                    break
            if flag:
                sum_ += i * 100
        elif np.sum(np.abs(grid[i] - grid[i - 1])) == 0:
            diff = 0
            for a, b in zip(range(i + 1, height), range(i - 2, -1, -1)):
                diff += np.sum(np.abs(grid[a] - grid[b]))
                if diff > 1:
                    break
            if diff == 1:
                sum_ += i * 100

    return sum_

def find_min_distance_of_all_pairs(file_path: str) -> int:
    """
    Find the minimum distance of all pairs in the puzzles from the given file.

    Parameters:
    - file_path (str): Path to the file containing the puzzles.

    Returns:
    - int: The sum of distances for all pairs.
    """
    sum_ = 0
    puzzles = parse_puzzle(file_path)

    for grid in puzzles:
        sum_ += check_symmetry(grid)

    return sum_

if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = find_min_distance_of_all_pairs(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The sum of all star distances is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
