"""
Advent of Code 2023 - Day 19, Part 1

Task: Parse instructions and find the sum of ratings of all accepted parts.
"""

import time

def calc_sum_rating(file_path: str) -> int:
    """
    Find the sum of ratings of all accepted parts.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - int: The sum of custom hash values.
    """
    with open(file_path, "r", encoding="utf8") as file:
        instructs, parts = file.read().split("\n\n")
        instruct_dict = {}
        ans = 0
        xmas_index = {"x": 0, "m": 1, "a": 2, "s": 3}

        for instruct in instructs.splitlines():
            instruct = instruct.strip()
            instruct_id = instruct[:instruct.index("{")]
            listify_instruct = instruct[instruct.index("{")+1:
                                        instruct.index("}")].split(",")
            instruct_dict[instruct_id] = listify_instruct

        for part in parts.splitlines():
            part = part.strip().replace("}", ",}")
            part = [int(_[:_.index(",")]) for _ in part.split("=")[1:]]

            next_instruct = "in"

            while True:
                for conditions in instruct_dict[next_instruct]:
                    if "<" in conditions:
                        xmas, val = conditions.split("<")
                        val, next_instruct = val.split(":")
                        if part[xmas_index[xmas]] < int(val):
                            break
                    elif ">" in conditions:
                        xmas, val = conditions.split(">")
                        val, next_instruct = val.split(":")
                        if part[xmas_index[xmas]] > int(val):
                            break
                    else:
                        next_instruct = conditions
                        break

                if next_instruct == "R":
                    break
                elif next_instruct == "A":
                    ans += sum(part)
                    break

        return ans

if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = calc_sum_rating(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The sum of ratings of all accepted parts is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
