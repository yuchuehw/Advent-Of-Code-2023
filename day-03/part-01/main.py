"""
Advent of Code 2023 - Day 3, Part 1

Task: Find the sum of all numbers (engine parts) that are adjacent to at least one symbol. A dot-symbol (.) is not considered a symbol in this exercise.
"""


def sum_of_engine_part(file_path: str) -> int:
    """
    Calculate the sum of all engine part numbers adjacent to at least one symbol in the engine schematic.

    Args:
        file_path (str): The path to the input file containing the engine schematic.

    Returns:
        int: The sum of all engine part numbers.
    """
    engine_part_sum = 0
    part_map = {}
    symbol_coord_list = []
    num = ""

    with open(file_path, "r", encoding="utf8") as file:
        for i, line in enumerate(file.readlines()):
            for j, chr in enumerate(line):
                if chr.isnumeric():
                    num += chr
                else:
                    if chr != "." and chr != "\n":
                        symbol_coord_list.append((i, j))
                    if num:
                        n = int(num)
                        coords_occupied = [(i, j - dec) for dec in range(1, len(num) + 1)]
                        for coord in coords_occupied:
                            part_map[coord] = [n] + coords_occupied
                        num = ""
            if num:
                n = int(num)
                coords_occupied = [(i, j - decrement) for decrement in range(len(num))]
                for coord in coords_occupied:
                    # include sibling coord for ease of deletion
                    part_map[coord] = [n] + coords_occupied
                num = ""

    for i, j in symbol_coord_list:
        neighbors = [(_, __) for _ in range(i + 2) for __ in range(j + 2)
                     if (i - 1 <= _ <= i + 1 and j - 1 <= __ <= j + 1)]

        for neighbor in neighbors:
            if neighbor in part_map:
                engine_part_sum += part_map[neighbor][0]
                # delete siblings
                for coord in part_map[neighbor][1:]:
                    if coord in part_map:
                        del part_map[coord]

    return engine_part_sum


if __name__ == "__main__":
    input_file_path = "input.txt"
    result = sum_of_engine_part(input_file_path)
    print(f"The sum of all engine parts is: {result}")
