"""
Advent of Code 2023 - Day 3, Part 2

Task: Find the gear ratio of every gear in the machine and add them all up.
"""


def sum_of_gear_ratio(file_path: str) -> int:
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
                    if chr == "*":
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
        neighbor_parts = []
        neighbor_siblings = []
        for neighbor in neighbors:
            if neighbor in part_map:
                neighbor_parts.append(part_map[neighbor][0])
                neighbor_siblings.append(part_map[neighbor][1:])
                # delete siblings
                for coord in part_map[neighbor][1:]:
                    if coord in part_map:
                        del part_map[coord]

        if len(neighbor_parts) == 2:
            engine_part_sum += neighbor_parts[0] * neighbor_parts[1]

        # restore the map for the next gear in case of gear stacking.
        for i, j in zip(neighbor_parts, neighbor_siblings):
            for coord in j:
                part_map[coord] = [i] + j

    return engine_part_sum


if __name__ == "__main__":
    input_file_path = "input.txt"
    result = sum_of_gear_ratio(input_file_path)
    print(f"The sum of all gear ratios is: {result}")
