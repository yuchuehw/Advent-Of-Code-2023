"""
Advent of Code 2023 - Day 11, Part 2

Task: Figure out the shortest distance of each pair of stars! empty row and column are now eq to 1000000 non empty row!
"""

import time
import numpy as np
from itertools import combinations


def find_min_distance_of_all_pairs(file_path: str) -> int:
    with open(file_path, "r", encoding="utf8") as file:
        galaxy_map = []
        stars = []

        for i, line in enumerate(file.readlines()):
            line = line.strip()
            row = []

            for j, char in enumerate(line):
                if char == "#":
                    stars.append((i, j))
                    row.append(1)
                else:
                    row.append(0)

            galaxy_map.append(row)

        galaxy_map = np.array(galaxy_map)
        empty_rows = [i for i in range(len(galaxy_map)) if sum(galaxy_map[i]) == 0]
        empty_cols = [j for j in range(len(galaxy_map[0])) if sum(galaxy_map[:, j]) == 0]

        sum_of_all_distance = 0

        for star_i, star_j in combinations(stars, 2):
            distance = 0

            a, b = min(star_i[0], star_j[0]), max(star_i[0], star_j[0])
            distance += sum(1 if i not in empty_rows else 1000000 for i in range(a + 1, b + 1, 1))

            a, b = min(star_i[1], star_j[1]), max(star_i[1], star_j[1])
            distance += sum(1 if j not in empty_cols else 1000000 for j in range(a + 1, b + 1, 1))

            sum_of_all_distance += distance

        return sum_of_all_distance


if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = find_min_distance_of_all_pairs(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The sum of all star distances is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
