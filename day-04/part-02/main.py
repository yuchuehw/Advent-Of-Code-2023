"""
Advent of Code 2023 - Day 4, Part 2

Task: Tally up the number of scratch cards you won! If a number matched on the kth card, you win an additional copy of k+1... to k+i card. But if you have multiple copies of the kth card, you get multiple copies of k+1... to k+i card!
"""


def sum_of_cards(file_path: str) -> int:
    """
    Calculate the total number of scratch cards won, considering the matching numbers.

    Args:
        file_path (str): The path to the input file containing scratch card information.

    Returns:
        int: The total number of scratch cards won.
    """
    with open(file_path, "r", encoding="utf8") as file:
        lines = file.readlines()
        cards = [1] * len(lines)
        for i, line in enumerate(lines):
            line = line.replace("  ", " ")  # Remove double space of single number to avoid slicing issues
            win_num, your_num = line[line.index(":") + 1:].strip().split("|")
            win_num = set(win_num.strip().split(" "))
            your_num = set(your_num.strip().split(" "))
            matches = len(win_num.intersection(your_num))

            if matches:
                for j in range(1, matches + 1):
                    cards[i + j] += cards[i]

        return sum(cards)


if __name__ == "__main__":
    input_file_path = "input.txt"
    result = sum_of_cards(input_file_path)
    print(f"The total number of scratch cards won is: {result}")
