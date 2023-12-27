"""
Advent of Code 2023 - Day 16, Part 1

Task: Ray tracing! Determine how many squares will be energized by the beam.
"""

import time

import sys

sys.setrecursionlimit(10000)

def energize(coord: tuple, dir: tuple, map: list, energize_map: list, prevent_repeat: set):
    """
    Recursively energize squares based on the given coordinates and direction.

    Parameters:
    - coord (tuple): Current coordinates (row, column).
    - dir (tuple): Direction vector (row_step, col_step).
    - map (list): Original map with beam directions.
    - energize_map (list): Map to mark energized squares.
    - prevent_repeat (set): Set to prevent revisiting coordinates.

    Returns:
    - None
    """
    width, height = len(map[0]), len(map)
    new_cord1, new_cord2, new_dir1, new_dir2 = None, None, None, None

    if map[coord[0]][coord[1]] == "." or (map[coord[0]][coord[1]] == "-" and (dir == (0, 1) or dir == (0, -1))) or \
            (map[coord[0]][coord[1]] == "|" and (dir == (1, 0) or dir == (-1, 0))):

        new_cord1 = (coord[0] + dir[0], coord[1] + dir[1])
        new_dir1 = dir

    elif map[coord[0]][coord[1]] == "-":
        new_cord1 = (coord[0], coord[1] + 1)
        new_dir1 = (0, 1)
        new_cord2 = (coord[0], coord[1] - 1)
        new_dir2 = (0, -1)

    elif map[coord[0]][coord[1]] == "|":
        new_cord1 = (coord[0] + 1, coord[1])
        new_dir1 = (1, 0)
        new_cord2 = (coord[0] - 1, coord[1])
        new_dir2 = (-1, 0)

    elif map[coord[0]][coord[1]] == "\\":
        new_dir1 = (dir[1] * 1, dir[0] * 1)
        new_cord1 = (coord[0] + new_dir1[0], coord[1] + new_dir1[1])

    elif map[coord[0]][coord[1]] == "/":
        new_dir1 = (dir[1] * -1, dir[0] * -1)
        new_cord1 = (coord[0] + new_dir1[0], coord[1] + new_dir1[1])

    if new_cord1:
        if 0 <= new_cord1[0] < height and 0 <= new_cord1[1] < width:
            energize_map[new_cord1[0]][new_cord1[1]] = 1
            next_gen = (new_cord1, new_dir1)
            if next_gen not in prevent_repeat:
                prevent_repeat.add(next_gen)
                energize(next_gen[0], next_gen[1], map, energize_map, prevent_repeat)

    if new_cord2:
        if 0 <= new_cord2[0] < height and 0 <= new_cord2[1] < width:
            energize_map[new_cord2[0]][new_cord2[1]] = 1
            next_gen = (new_cord2, new_dir2)
            if next_gen not in prevent_repeat:
                prevent_repeat.add(next_gen)
                energize(next_gen[0], next_gen[1], map, energize_map, prevent_repeat)


def calc_total_energized(file_path: str) -> int:
    """
    Calculate the total number of energized squares based on the input map.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - int: The sum of all energized squares.
    """
    with open(file_path, "r", encoding="utf8") as file:
        map = [list(line.strip()) for line in file.readlines()]
        energize_map = [[0] * len(map[0]) for _ in range(len(map))]
        energize_map[0][0] = 1
        energize((0, 0), (0, 1), map, energize_map, set())
    return sum([sum(row) for row in energize_map])


if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = calc_total_energized(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The sum of all energized squares is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
