"""
Advent of Code 2023 - Day 2, Part 2

Task: Read a file and determine the minimum amount of each ball required and the power they have. Sum up all the power.
"""

from functools import reduce


def calculate_power(game_str: str) -> int:
    """
    Calculate the power of the minimum set of cubes required for a game.

    Args:
        game_str (str): String representing a game record.

    Returns:
        int: The power of the minimum set of cubes.
    """
    if "Game" not in game_str or ":" not in game_str:
        return 0

    game_str = game_str[game_str.index(":") + 1:].strip()
    min_requirement = {}

    for round in game_str.split(";"):
        for balls in round.split(","):
            quantity = "".join(filter(str.isdigit, balls))
            color = "".join(filter(str.isalpha, balls)).strip()

            quantity = int(quantity)
            if color not in min_requirement or min_requirement[color] < quantity:
                min_requirement[color] = quantity

    return reduce(lambda a, b: a * b, min_requirement.values(), 1)


def sum_of_all_power(file_path: str) -> int:
    """
    Calculate the sum of power for all games in the given file.

    Args:
        file_path (str): The path to the input file.

    Returns:
        int: The sum of power for all games.
    """
    sum_power = 0

    with open(file_path, "r", encoding="utf8") as file:
        for line in file.readlines():
            sum_power += calculate_power(line)

    return sum_power


if __name__ == "__main__":
    input_file_path = "input.txt"
    result = sum_of_all_power(input_file_path)
    print(f"The sum of power for all games is: {result}")
