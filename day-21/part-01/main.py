"""
Advent of Code 2023 - Day 21, Part 1

Task: Circuit simulation. count the high and low pulses when button is pressed 1000 times.
"""

import time
import numpy as np

def simulate_circuit(file_path: str) -> int:
    """
    Build and simulate circuit after 1000 button press.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - int: The sum of custom hash values.
    """
    with open(file_path, "r", encoding="utf8") as file:
        map = []
        start_pos = [0,0]
        for i, line in enumerate(file.readlines()):
            if "S" in line:
                start_pos[0] = i
                start_pos[1] = line.index("S")

            map.append(list(line.strip()))
        # print(start_pos)
        # print(*map,sep="\n")
        start_pos = tuple(start_pos)
        curr_gen = {start_pos}
        next_gen = set()
        width = len(map[0])
        height = len(map)
        STEPS_ALLOWED = 26501365
        for _ in range(STEPS_ALLOWED):
            for x,y in curr_gen:
                neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                for point in neighbors:
                    i,j = point
                    if 0<=i<height and 0<=j<width and map[i][j] != "#":
                        next_gen.add(point)
            curr_gen = next_gen
            next_gen = set()
        return(len(curr_gen))
                    
if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = simulate_circuit(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The squares reachable after exactly 64 stpeps are {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
