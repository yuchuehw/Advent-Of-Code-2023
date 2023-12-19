"""
Advent of Code 2023 - Day 2, Part 1

Task: Read a file and determine the number of games that are possible given the initial balls quantity and colors. Sum the game numbers that are possible.
"""


def is_possible_game(start_pos: dict, game_str: str) -> bool:
    """
    Check if a game is possible based on the initial ball quantities and colors.

    Args:
        start_pos (dict): Dictionary representing the initial ball quantities and colors.
        game_str (str): String representing a game record.

    Returns:
        bool: True if the game is possible, False otherwise.
    """
    if "Game" not in game_str or ":" not in game_str:
        return False

    game_str = game_str[game_str.index(":") + 1:].strip()
    for round in game_str.split(";"):
        combo = {}
        for balls in round.split(","):
            quantity = "".join(filter(str.isdigit, balls))
            color = "".join(filter(str.isalpha, balls)).strip()

            combo[color] = int(quantity)

        for color in combo:
            if color not in start_pos or combo[color] > start_pos[color]:
                return False

    return True


def sum_of_possible_game_ids(file_path: str, start_pos: dict) -> int:
    """
    Calculate the sum of game IDs that are possible based on the initial ball quantities and colors.

    Args:
        file_path (str): The path to the input file.
        start_pos (dict): Dictionary representing the initial ball quantities and colors.

    Returns:
        int: The sum of game IDs for possible games.
    """
    total_sum = 0

    with open(file_path, "r", encoding="utf8") as file:
        for i, line in enumerate(file.readlines()):
            if is_possible_game(start_pos, line):
                total_sum += i + 1

    return total_sum


if __name__ == "__main__":
    input_file_path = "input.txt"
    start_pos = {'red': 12, 'green': 13, 'blue': 14}
    result = sum_of_possible_game_ids(input_file_path, start_pos)
    print(f"The sum of IDs of all possible games is: {result}")
