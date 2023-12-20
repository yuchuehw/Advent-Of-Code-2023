"""
Advent of Code 2023 - Day 5, Part 1

Task: Using the crazy lookup table to find the seed with the smallest location number. actually seeds are written in start, range pair, so now try solve this problem again!
"""

def lookup(translate_table: dict, from_to_pair: tuple, id_range_pair: tuple) -> list:
    """
    Perform a lookup using the translation table to convert from one category to another.

    Args:
        translate_table (dict): The translation table containing conversion rules.
        from_to_pair (tuple): A pair of categories (source and destination) to look up in the table.
        id_range_pair (tuple): The initial identifier and its range.

    Returns:
        list: The converted identifier in id-range pair.
    """
    if from_to_pair not in translate_table:
        raise KeyError("Lookup table does not exist")

    start, end = id_range_pair[0], id_range_pair[0] + id_range_pair[1] - 1

    new_id_range_pair = []

    for a, b, c in translate_table[from_to_pair]:
        if a <= start <= b:
            if a <= end <= b:
                new_id_range_pair.append((start - a + c, end - start + 1))
                return new_id_range_pair
            else:
                new_id_range_pair.append((start - a + c, b - start + 1))
                start = b + 1
        elif start < a:
            if end < a:
                new_id_range_pair.append((start, end - start + 1))
                return new_id_range_pair
            else:
                new_id_range_pair.append((start, a - start))
                if end < b:
                    new_id_range_pair.append((c, end - a + 1))
                    return new_id_range_pair
                else:
                    new_id_range_pair.append((c, b - a + 1))
                    start = b + 1

    # If still not returned?
    new_id_range_pair.append((start, end - start + 1))
    return new_id_range_pair

def reorganize_data(file_path: str) -> tuple:
    """
    Read the input file and organize the data.

    Args:
        file_path (str): The path to the input file.

    Returns:
        tuple: A tuple containing the list of seeds and the translation table.
    """
    with open(file_path, "r", encoding="utf8") as file:
        seeds, *tables = file.read().split("\n\n")

    raw_seeds_data = [int(_) for _ in seeds[seeds.index(":") + 1:].strip().split(" ")]

    seeds_pair = zip(raw_seeds_data[::2], raw_seeds_data[1::2])

    translate_table = {}

    for table in tables:
        from_, to_ = table[:table.index(" ")].split("-to-")
        procedure = translate_table[(from_, to_)] = []
        for line in table.splitlines()[1:]:
            line = line.strip()
            to_id, from_id, range_ = line.split(" ")
            to_id, from_id, range_ = int(to_id), int(from_id), int(range_)

            procedure.append((from_id, from_id + range_ - 1, to_id))

        procedure.sort()

    return seeds_pair, translate_table

def find_min_via_steps(id_range_pair_list: list, steps: list, translate_table: dict) -> int:
    """
    Find the minimum location number corresponding to the initial seeds after multiple conversions.

    Args:
        id_range_pair_list (list): The list of initial seed numbers and their ranges.
        steps (list): The conversion steps to perform in order.
        translate_table (dict): The translation table containing conversion rules.

    Returns:
        int: The minimum location number.
    """
    for step in steps:
        next_id_range_pair = []
        for id_range_pair in id_range_pair_list:
            _ = lookup(translate_table, step, id_range_pair)
            next_id_range_pair.extend(_)
        id_range_pair_list = next_id_range_pair

    return min((_[0] for _ in next_id_range_pair))

if __name__ == "__main__":
    input_file_path = "input.txt"
    seeds_pair, translate_table = reorganize_data(input_file_path)

    result = find_min_via_steps(
        seeds_pair,
        [
            ("seed", "soil"),
            ("soil", "fertilizer"),
            ("fertilizer", "water"),
            ("water", "light"),
            ("light", "temperature"),
            ("temperature", "humidity"),
            ("humidity", "location"),
        ],
        translate_table,
    )

    print(f"The min location is: {result}")
