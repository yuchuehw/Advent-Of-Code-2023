"""
Advent of Code 2023 - Day 5, Part 1

Task: Using the crazy lookup table to find the seed with the smallest location number
"""

def lookup(translate_table: dict, from_to_pair: tuple, from_id: int) -> int:
    """
    Perform a lookup using the translation table to convert from one category to another.

    Args:
        translate_table (dict): The translation table containing conversion rules.
        from_to_pair (tuple): A pair of categories (source and destination) to look up in the table.
        from_id (int): The initial identifier to convert.

    Returns:
        int: The converted identifier.
    """
    if from_to_pair not in translate_table:
        raise KeyError("Lookup table does not exist")

    for a, b, c in translate_table[from_to_pair]:
        if a <= from_id <= b:
            return (from_id - a) + c

    return from_id

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

    seeds = [int(_) for _ in seeds[seeds.index(":") + 1:].strip().split(" ")]

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

    return seeds, translate_table

def find_min_via_steps(seeds, steps, translate_table):
    """
    Find the minimum location number corresponding to the initial seeds after multiple conversions.

    Args:
        seeds (list): The list of initial seed numbers.
        steps (list): The conversion steps to perform in order.
        translate_table (dict): The translation table containing conversion rules.

    Returns:
        int: The minimum location number.
    """
    final = []
    for id_ in seeds:
        for step in steps:
            id_ = lookup(translate_table, step, id_)
        final.append(id_)

    return min(final)

if __name__ == "__main__":
    input_file_path = "input.txt"
    seeds, translate_table = reorganize_data(input_file_path)

    result = find_min_via_steps(
        seeds,
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
