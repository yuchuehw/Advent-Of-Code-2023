"""
Advent of Code 2023 - Day 19, Part 1

Task: parse instructions and find the combinations of accepted parts!
"""

from collections import namedtuple
import time
import copy
import functools
import operator

def calc_sum_rating(file_path: str) -> int:
    """
    Find the sum of rating of all accepted parts

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - int: The sum of custom hash values.
    """
    with open(file_path, "r", encoding="utf8") as file:
        instructs, parts = file.read().split("\n\n")
        instruct_dict = {}


        ans = 0

        xmas_index = {"x":0,"m":1,"a":2,"s":3}

        for instruct in instructs.splitlines():
            instruct = instruct.strip()
            instruct_id = instruct[:instruct.index("{")]
            listify_instruct = instruct[instruct.index("{")+1:
                                        instruct.index("}")].split(",")
            instruct_dict[instruct_id] = listify_instruct



        def create_fork(instruct_id, range_):
            ans = 0
            for conditions in instruct_dict[instruct_id]:
                if "<" in conditions:
                    xmas, val = conditions.split("<")
                    val, next_instruct = val.split(":")
                    val = int(val)
                    frange = copy.deepcopy(range_)
                    frange[xmas_index[xmas]][1] = val - 1
                    range_[xmas_index[xmas]][0] = val

                    if next_instruct == "A":
                        ans += functools.reduce(operator.mul, [j-i+1 for i,j in frange])

                    elif next_instruct == "R":
                        ans += 0
                    else:
                        ans += create_fork(next_instruct, frange)
                
                elif ">" in conditions:
                    xmas, val = conditions.split(">")
                    val, next_instruct = val.split(":")
                    val = int(val)
                    frange = copy.deepcopy(range_)
                    frange[xmas_index[xmas]][0] = val + 1
                    range_[xmas_index[xmas]][1] = val

                    if next_instruct == "A":
                        ans += functools.reduce(operator.mul, [j-i+1 for i,j in frange])
                    elif next_instruct == "R":
                        ans += 0
                    else:
                        ans += create_fork(next_instruct, frange)
                else:
                    next_instruct = conditions
                    if next_instruct == "A":
                        ans += functools.reduce(operator.mul, [j-i+1 for i,j in range_])
                    elif next_instruct == "R":
                        ans += 0
                    else:
                        ans += create_fork(next_instruct, range_)
            return ans
        return create_fork("in", [[1,4000] for _ in range(4)])
        

if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = calc_sum_rating(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The area of this map is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
