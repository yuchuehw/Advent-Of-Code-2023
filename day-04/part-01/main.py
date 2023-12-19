"""
Advent of Code 2023 - Day 4, Part 1

Task: Calculate the point of scratch cards. Scratch card points are calculated as 2**(n-1) where n is the number of matching numbers on the winning side (left to the |) and your side (right to the |).
"""


def sum_of_points(file_path: str) -> int:
    """
    Calculate the total points of the scratch cards based on matching numbers with the winning numbers.

    Args:
        file_path (str): The path to the input file containing scratch card information.

    Returns:
        int: The total points of all scratch cards.
    """
    point_sum = 0

    with open(file_path, "r", encoding="utf8") as file:
        for line in file.readlines():
            line = line.replace("  ", " ")  # Remove double space of single number to avoid slicing issues
            win_num, your_num = line[line.index(":") + 1:].strip().split("|")
            win_num = set(win_num.strip().split(" "))
            your_num = set(your_num.strip().split(" "))
            matches = len(win_num.intersection(your_num))

            if matches:
                point_sum += 2 ** (matches - 1)

    return point_sum


if __name__ == "__main__":
    input_file_path = "input.txt"
    result = sum_of_points(input_file_path)
    print(f"The sum of all gear ratios is: {result}")
