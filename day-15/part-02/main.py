"""
Advent of Code 2023 - Day 15, Part 2

Task: Hashing the message and working with a hashmap!
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


def find_min_distance_of_all_pairs(file_path: str) -> int:
    """
    Calculate the sum of distances based on a hashmap.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - int: The sum of distances.
    """
    with open(file_path, "r", encoding="utf8") as file:
        boxes = [[{}, 0] for _ in range(256)]
        for message in file.readline().strip().split(","):
            if "=" in message:
                label, power = message.split("=")
                box_no = custom_hash(label)
                if label in boxes[box_no][0]:
                    boxes[box_no][0][label][0] = int(power)
                else:
                    boxes[box_no][0][label] = [int(power), boxes[box_no][1]]
                    boxes[box_no][1] += 1

            elif "-" in message:
                label = message.split("-")[0]
                box_no = custom_hash(label)
                if label in boxes[box_no][0]:
                    del boxes[box_no][0][label]
                else:
                    pass
            else:
                raise Exception("PANIC")

        total_sum = 0
        for box_no in range(256):
            for i, lens_info in enumerate(sorted(boxes[box_no][0].items(), key=lambda _: _[1][1])):
                power = lens_info[1][0]
                total_sum += (box_no + 1) * (i + 1) * power

        return total_sum


if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = find_min_distance_of_all_pairs(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The sum of all star distances is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
