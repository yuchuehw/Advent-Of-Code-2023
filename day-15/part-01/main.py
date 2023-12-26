"""
Advent of Code 2023 - Day 15, Part 1

Task: Hashing the message and summing them!
"""

import time

def custom_hash(string: str) -> int:
    """
    Custom hash function that iterates over characters in the string.

    Parameters:
    - string (str): Input string to be hashed.

    Returns:
    - int: The hashed result.
    """
    hash_result = 0
    for character in string:
        hash_result += ord(character)
        hash_result *= 17
        hash_result %= 256

    return hash_result


def calculate_sum_of_hashes(file_path: str) -> int:
    """
    Calculate the sum of custom hashes for messages read from a file.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - int: The sum of custom hash values.
    """
    with open(file_path, "r", encoding="utf8") as file:
        total_sum = 0
        messages = file.readline().strip().split(",")

        for message in messages:
            total_sum += custom_hash(message)

    return total_sum


if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = calculate_sum_of_hashes(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The sum of all custom hash values is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
