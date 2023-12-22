"""
Advent of Code 2023 - Day 10, Part 1

Task: Can you solve this maze! Find the longest distance to travel from the start of the maze to the furthest poin of the loop!
"""

import time

# Coordinate system (row, col) where positive is down right.
symbol_to_dir_map = {
    "|" : ((-1, 0), (1, 0)),  # How neighbor square comes into this square.
    "-" : ((0, 1), (0, -1)),
    "L" : ((1, 0), (0, -1)),
    "J" : ((1, 0), (0, 1)),
    "7" : ((-1, 0), (0, 1)),
    "F" : ((-1, 0), (0, -1)),
    "S" : ((1, 0), (-1, 0), (0, -1), (0, 1)),
    "." : ((0, 0))
}

def traverse_pipes(pipe_map, previous_move, start_point):
    """
    Traverse the pipes and calculate the distance to reach the farthest point in the loop.
    """
    steps = 1
    current_point = start_point

    for _ in range(100000):  # A reasonable upper bound for the puzzle
        point_connections = pipe_map[current_point[0]][current_point[1]]
        
        if len(point_connections) == 4:
            return steps
        elif previous_move == point_connections[0]:
            current_point = (
                current_point[0] - point_connections[1][0],
                current_point[1] - point_connections[1][1]
            )
            previous_move = (
                -point_connections[1][0],
                -point_connections[1][1]
            )
        elif previous_move == point_connections[1]:
            current_point = (
                current_point[0] - point_connections[0][0],
                current_point[1] - point_connections[0][1]
            )
            previous_move = (
                -point_connections[0][0],
                -point_connections[0][1]
            )
        else:
            return

        steps += 1

    return

def expanded_triangle_sum(file_path: str) -> int:
    with open(file_path, "r", encoding="utf8") as file:
        pipe_map = []
        start_points = []

        for i, line in enumerate(file.readlines()):
            if "S" in line:
                start_points.append((i, line.index("S")))

            pipe_map.append([symbol_to_dir_map[chr] for chr in line if chr != "\n"])

        if not start_points:
            return
        
        loop_lengths = []

        for start_point in start_points:
            for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if direction in pipe_map[start_point[0] + direction[0]][start_point[1] + direction[1]]:
                    loop_length = traverse_pipes(
                        pipe_map, direction, (start_point[0] + direction[0], start_point[1] + direction[1])
                    )

                    if loop_length:
                        loop_lengths.append(loop_length)

        print(loop_lengths)
        return max(loop_lengths) // 2

if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = expanded_triangle_sum(input_file_path)
    end_time = time.time()  # Record the end time

    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The sum of all the expanded triangles is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
