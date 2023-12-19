"""
Advent of Code 2023 - Day 1, Part 2

Task: Read a file and return the sum of digits made up by each line.
The number made by each line is defined to be the first digit multiplied by ten and added with the last digit. (Number can be algebraic or spelled out.)
"""
from collections import defaultdict
from typing import Dict, List


NUMBERS: Dict[str, int] = {str(i): i for i in range(10)}

SPELLED_OUT_NUMBERS: Dict[str, int] = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def locate_candidates(
    cand_num_pair: Dict[str, int],
    string_to_search: str,
    candidates: defaultdict
) -> None:
    """
    Helper function to locate candidate numbers in a string.

    Args:
        cand_num_pair (Dict[str, int]): Dictionary of numbers and their integer representations.
        string_to_search (str): The string to search for candidate numbers.
        candidates (defaultdict): Dictionary to store candidate locations.
    """
    for num in cand_num_pair:
        try:
            cand_loc_first = string_to_search.index(num)
            cand_loc_last = string_to_search.rindex(num)
            candidates[cand_num_pair[num]].append(cand_loc_first)
            candidates[cand_num_pair[num]].append(cand_loc_last)
        except ValueError:
            pass


def calculate_calibration_sum(file_path: str) -> int:
    """
    Calculate the sum of calibration values based on the given file.

    Args:
        file_path (str): The path to the input file.

    Returns:
        int: The sum of calibration values.
    """
    total_sum = 0

    with open(file_path, "r", encoding="utf8") as file:
        for line in file.readlines():
            candidates: defaultdict = defaultdict(list)

            locate_candidates(NUMBERS, line, candidates)
            locate_candidates(SPELLED_OUT_NUMBERS, line, candidates)

            min_num: int = None
            global_min: int = len(line)
            for num, occurrence_indexes in candidates.items():
                num_min = min(occurrence_indexes)
                if num_min < global_min:
                    global_min = num_min
                    min_num = num

            total_sum += min_num * 10

            max_num: int = None
            global_max: int = -1
            for num, occurrence_indexes in candidates.items():
                num_max = max(occurrence_indexes)
                if num_max > global_max:
                    global_max = num_max
                    max_num = num

            total_sum += max_num

            # Print the two-digit number formed by the first and last digits
            print(min_num * 10 + max_num)

    return total_sum


if __name__ == "__main__":
    input_file_path = "input.txt"
    result = calculate_calibration_sum(input_file_path)
    print(f"The sum of calibration values is: {result}")
