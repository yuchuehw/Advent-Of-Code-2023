"""
Advent of Code 2023 - Day 8, Part 2

Task: Using the provided network of nodes and left/right instructions, determine the number of steps required to get from xxA to xxZ.
"""
from math import lcm
import time


def plan_route(file_path: str, start_point_ending, end_point_ending) -> int:
    """
    Read the input file and determine the number of steps required to get from start_point to end_point.

    Args:
        file_path (str): The path to the input file.
        start_point_ending (str): All point with this ending in the network.
        end_point_ending (str): Any point with this the network.

    Returns:
        int: The number of steps required to reach the end_point from the start_point.
    """
    with open(file_path, "r", encoding="utf8") as file:
        directions, relationships = file.read().split("\n\n")

        relation_dict = {}
        start_points = set()
        end_points = set()

        for line in relationships.splitlines():
            point = line[:3]
            left_neighbor = line[7:10]
            right_neighbor = line[12:15]
            assert point not in relation_dict
            relation_dict[point] = (left_neighbor, right_neighbor)
            if point.endswith(start_point_ending):
                start_points.add(point)
            if point.endswith(end_point_ending):
                end_points.add(point)

        assert len(start_points) and len(end_points)


        # the naive solution does not work and require way too much time to compute
        # steps = 0
        # current_points = start_points
        # next_points = set()
        # while True:  # Ensure a reasonable limit to avoid infinite loops
        #     for char in directions:
        #         # print(current_points)
        #         if current_points.issubset(end_points):
        #             print(current_points)
        #             return steps
        #         for point in current_points:
        #             if char == "L":
        #                 next_points.add(relation_dict[point][0])

        #             elif char == "R":
        #                 next_points.add(relation_dict[point][1])
        #         current_points = next_points
        #         next_points = set()
        #         steps += 1

        
        step_for_each = []
        for start_point in start_points:
            steps = 0
            current_points = {start_point}
            next_points = set()
            for x in range(1000):  # Ensure a reasonable limit to avoid infinite loops
                flag = False
                for char in directions:
                    # print(current_points)
                    if current_points.issubset(end_points):
                        print(current_points)
                        flag = True
                        break
                    for point in current_points:
                        if char == "L":
                            next_points.add(relation_dict[point][0])
            
                        elif char == "R":
                            next_points.add(relation_dict[point][1])
                    current_points = next_points
                    next_points = set()
                    steps += 1
                if flag:
                    break
            step_for_each.append(steps)
        return lcm(*step_for_each)
if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    steps = plan_route(input_file_path, "A", "Z")
    end_time = time.time()  # Record the end time

    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"According to the map, it takes {steps} steps to all XXA to XXZ")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
