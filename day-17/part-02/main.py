"""
Advent of Code 2023 - Day 17, Part 2

Task: Write a path finding algorithm to minimize heat loss!
"""

import time
import heapq

DIRECTIONS = {
    (1, 0): [(1, 0), (0, 1), (0, -1)],
    (-1, 0): [(-1, 0), (0, 1), (0, -1)],
    (0, 1): [(0, 1), (1, 0), (-1, 0)],
    (0, -1): [(0, -1), (1, 0), (-1, 0)],
    None: [(0, 1), (0, -1), (1, 0), (-1, 0)]
}

def calculate_min_heat_lost(file_path: str) -> int:
    with open(file_path, "r", encoding="utf8") as file:
        ht_lst_mp = [list(map(int, line.strip())) for line in file.readlines()]

    width, height = len(ht_lst_mp[0]), len(ht_lst_mp)
    que = [(0, (0, 0), None, 0)]  # Add a counter for consecutive moves
    visited = dict()

    while que:
        score, point, last_dir, consecutive_moves = heapq.heappop(que)

        if (point, last_dir, consecutive_moves) in visited:
            continue
            
        visited[(point, last_dir, consecutive_moves)] = score

 
        
        directions = [last_dir] if consecutive_moves < 4 and last_dir != None else DIRECTIONS[last_dir] 
        
        for dir in directions:
            
            new_point = (point[0] + dir[0], point[1] + dir[1])
            new_consecutive_moves = consecutive_moves + 1 if dir == last_dir else 1
            if (
                0 <= new_point[0] < height and 0 <= new_point[1] < width and
                new_point not in visited and new_consecutive_moves <= 10

            ):
                new_score = score + ht_lst_mp[new_point[0]][new_point[1]]

                heapq.heappush(que, (new_score, new_point, dir, new_consecutive_moves))

    score = 1e100
    for k,v in visited.items():
        point, _, consecutive_moves = k
        if point == (height - 1, width - 1) and consecutive_moves >= 4:
            score = min(score, v)

    return score

if __name__ == "__main__":

    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = calculate_min_heat_lost(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The route with the least heat lost has a heat loss of {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
