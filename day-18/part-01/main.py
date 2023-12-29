"""
Advent of Code 2023 - Day 18, Part 1

Task: draw a map following the direction and calculate the area bounded by the map.
"""

import time
import numpy as np

import sys

sys.setrecursionlimit(10000)

def calculate_min_heat_lost(file_path: str) -> int:
    """
    Find the area bounded by the map.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - int: The sum of custom hash values.
    """
    with open(file_path, "r", encoding="utf8") as file:
        map = np.array([[1]])
        width = 1
        height = 1
        index = [0, 0]
        for line in file.readlines():
            dir, steps, _ = line.strip().split(" ")
            increments = (0,0)
            if dir == "R":
                increments = (0,1)
            elif dir == "L":
                increments = (0,-1)
            elif dir == "D":
                increments = (1,0)
            elif dir == "U":
                increments = (-1,0)

            for i in range(int(steps)):
                index = [index[0]+increments[0], index[1]+increments[1]]
                if 0 <= index[0] < height and 0 <= index[1] < width:
                    map[index[0]][index[1]] = 1
                elif index[0] == -1:
                    temp = np.zeros((height+1,width))
                    temp[1:] = map
                    map = temp
                    map[0][index[1]] = 1
                    index[0] = 0
                    height += 1
                elif index[0] == height:
                    temp = np.zeros((height+1,width))
                    temp[:-1] = map
                    map = temp
                    map[index[0]][index[1]] = 1
                    height += 1
                elif index[1] == -1:
                    temp = np.zeros((height,width+1))
                    temp[:,1:] = map
                    map = temp
                    map[index[0]][0] = 1
                    index[1] = 0
                    width += 1
                elif index[1] == width:
                    temp = np.zeros((height,width+1))
                    temp[:,:-1] = map
                    map = temp
                    map[index[0]][index[1]] = 1
                    width += 1
                else:
                    raise Exception("PANIC")
        map2 = [[(2 if (i==0 or i== height-1 or j==0 or j==width-1) else 0)for j in range(width)] for i in range(height)]

        def generate_neighbor(px,py,w,h):
            return [(i,j) for i in range(px-1,px+2) 
                    for j in range (py-1,py+2) 
                    if i>= 0 and j >= 0 and i < h and j < w]
        
        def infect_neighbor(m, point,w,h):
            try:
                neighbors = generate_neighbor(point[0],point[1],w,h)
                for i, j in neighbors:
                    if m[i][j] == 0:
                        m[i][j] = 2
                        success = infect_neighbor(m, (i,j),w,h)
                        if not success:
                            return False
                return True
            except RecursionError:
                return False
        for i in range(height):
            for j in range(width):
                if map[i][j] == 1:
                    map2[i][j] = 1


        flag = False
        
        for _ in range(10):
            restart = False
            if not flag:
                for i in range(height):
                    for j in range(width):
                        if map2[i][j] == 2:
                            flag = infect_neighbor(map2,(i,j),width,height)
                            if not flag:
                                restart = True
                                break
                    if restart:
                        break
            else:
                break
        if not flag:
            return None
        return width*height - sum([map2[i].count(2) for i in range(height)])

if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = calculate_min_heat_lost(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The area of this map is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
