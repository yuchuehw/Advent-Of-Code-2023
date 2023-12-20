"""
Advent of Code 2023 - Day 8, Part 1

Task: Using the provided network of nodes and left/right instructions, determine the number of steps required to get from AAA to ZZZ.
"""

def plan_route(file_path: str, start_point, end_point) -> int:
    """
    Read the input file and determine the number of steps required to get from start_point to end_point.

    Args:
        file_path (str): The path to the input file.
        start_point (str): The starting point in the network.
        end_point (str): The destination point in the network.

    Returns:
        int: The number of steps required to reach the end_point from the start_point.
    """
    with open(file_path, "r", encoding="utf8") as file:
        directions, relationships = file.read().split("\n\n")
        
        relation_dict = {}
        
        for line in relationships.splitlines():
            point = line[:3]
            left_neighbor = line[7:10]
            right_neighbor = line[12:15]
            assert point not in relation_dict
            relation_dict[point] = (left_neighbor, right_neighbor)

        assert start_point in relation_dict and end_point in relation_dict 
        current_point = start_point
        steps = 0

        for x in range(1000):  # Ensure a reasonable limit to avoid infinite loops
            for char in directions:
                if current_point == end_point:
                    return steps
                if char == "L":
                    current_point = relation_dict[current_point][0]
                    steps += 1
                elif char == "R":
                    current_point = relation_dict[current_point][1]
                    steps += 1
    
    return steps

if __name__ == "__main__":
    input_file_path = "input.txt"
    steps = plan_route(input_file_path, "AAA", "ZZZ")
    print(f"According to the map, it takes {steps} steps to get from AAA to ZZZ")
