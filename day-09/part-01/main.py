"""
Advent of Code 2023 - Day 9, Part 1

Task: Solving gaussian triangle. You are provided row one of each triangle. you need to predict the next number in the row! sum up all these values for all triangles.
"""

import time

def expanded_triangle_sum(file_path: str) -> int:
    """
    Calculate the sum of extrapolated values for each triangle in the given input.

    Args:
        file_path (str): The path to the input file.

    Returns:
        int: The sum of extrapolated values.
    """
    with open(file_path, "r", encoding="utf8") as file:
        sum_ = 0
        for line in file.readlines():
            layers = []
            layers.append([int(_) for _ in line.strip().split(" ")])
            flag = False
            while not flag:
                layer = []
                for index in range(1, len(layers[-1])):
                    layer.append(layers[-1][index] - layers[-1][index - 1])
                layers.append(layer)
                if len(set(layer)) == 1:
                    flag = True
            for i in range(len(layers) - 1, 0, -1):
                layers[i - 1].append(layers[i][-1] + layers[i - 1][-1])
            sum_ += layers[0][-1]
        return sum_

if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = expanded_triangle_sum(input_file_path)
    end_time = time.time()  # Record the end time

    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The sum of all the expanded triangles is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
