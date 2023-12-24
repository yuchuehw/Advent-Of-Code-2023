"""
Advent of Code 2023 - Day 13, Part 1

Task: Finding complete reflections and "summarize" them (sum of vert-symmetry + sum of hori-symmetry * 100)
"""

import time
import numpy as np


def find_min_distance_of_all_pairs(file_path: str) -> int:
    with open(file_path, "r", encoding="utf8") as file:
        total_sum = 0
        for puzzle in file.read().split("\n\n"):
            grid = [list(line.strip()) for line in puzzle.splitlines()]
            grid = np.array(grid)

            # check for vertical symmetry
            complete_vert_sym = []
            complete_hori_sym = []
            width = grid.shape[1]

            for j in range(1, width):
                if (grid[:, j] == grid[:, (j - 1)]).all():
                    flag = True
                    positions = zip(range(j, width), range(j - 1, -1, -1))

                    for a, b in positions:
                        if not (grid[:, a] == grid[:, b]).all():
                            flag = False
                            break

                    if flag:
                        total_sum += j

            # check for horizontal symmetry
            height = grid.shape[0]

            for i in range(1, height):
                if (grid[i] == grid[i - 1]).all():
                    flag = True
                    positions = zip(range(i, height), range(i - 1, -1, -1))

                    for a, b in positions:
                        if not (grid[a] == grid[b]).all():
                            flag = False
                            break

                    if flag:
                        total_sum += i * 100

        return total_sum


if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = find_min_distance_of_all_pairs(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The sum of all star distances is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
