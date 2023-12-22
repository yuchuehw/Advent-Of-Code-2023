"""
Advent of Code 2023 - Day 10, Part 2

Task: Find the number of tile that is enclosed by the loop.
"""

import time

import sys

sys.setrecursionlimit(50000)


### coord system (row, col). where positive is down right.

symbol_to_dir_map = {
    "|" : ((-1, +0), (+1, +0)), #how neighbor square come into this square.
    "-" : ((+0, +1), (+0, -1)),
    "L" : ((+1, +0), (+0, -1)),
    "J" : ((+1, +0), (+0, +1)),
    "7" : ((-1, +0), (+0, +1)),
    "F" : ((-1, +0), (+0, -1)),
    "S" : ((+1, +0), (-1, +0), (0, -1), (0, +1)),
    "." : ((+0, +0))
}



def treverse_pipes(map:list, previous_move:tuple, start_point) -> int:

    # print("*")
    steps = 1
    current_point = start_point
    allowed_points = []
    for x in range(100000): # a reasonable upper bound for the puzzle
        # print(current_point)
        allowed_points.append(current_point)
        point_connections = map[current_point[0]][current_point[1]]
        if len(point_connections) == 4:
            # print(allowed_points)
            return allowed_points
        elif previous_move == point_connections[0]:
            current_point = (current_point[0]-point_connections[1][0], current_point[1]-point_connections[1][1])
            previous_move = (-point_connections[1][0], -point_connections[1][1])
        elif previous_move == point_connections[1]:
            current_point = (current_point[0]-point_connections[0][0], current_point[1]-point_connections[0][1])
            previous_move = (-point_connections[0][0], -point_connections[0][1])
        else:
            return

        steps += 1
    return


def expanded_triangle_sum(file_path: str) -> int:
    with open(file_path, "r", encoding="utf8") as file:
        map = []
        start_point = []
        for i, line in enumerate(file.readlines()):
            if "S" in line:
                start_point.append((i,line.index("S")))
            map.append([symbol_to_dir_map[chr] for chr in line if chr != "\n"])

        if not start_point:
            return
        loop_lengths = []
        
        for start in start_point:
            start_piece = []
            if (-1,+0) in map[start[0]-1][start[1]+0]:
                loop_length = treverse_pipes(map, (-1,+0), (start[0]-1, start[1]+0))
                if loop_length:
                    loop_lengths.append(loop_length)
                    start_piece.append((+1,+0))
            if (+1,+0) in map[start[0]+1][start[1]+0]:
                loop_length = treverse_pipes(map, (+1,+0), (start[0]+1, start[1]+0))
                if loop_length:
                    loop_lengths.append(loop_length)
                    start_piece.append((-1,+0))
            if (+0,+1) in map[start[0]+0][start[1]+1]:
                loop_length = treverse_pipes(map, (+0,+1), (start[0]+0, start[1]+1))
                if loop_length:
                    loop_lengths.append(loop_length)
                    start_piece.append((+0,-1))
            if (+0, -1) in map[start[0]+0][start[1]-1]:
                loop_length = treverse_pipes(map, (+0,-1), (start[0]+0, start[1]-1))
                if loop_length:
                    loop_lengths.append(loop_length)
                    start_piece.append((+0,+1))
            # print(start_piece)
            map[start[0]][start[1]] = tuple(start_piece)
        # print(loop_lengths)
        width = len(map[0])
        height = len(map)
        
        # a new map to define inside(0) the loop, outside(1) the loop, or pipe(2)
        # the border of the map is gurantee to be outside or pipe.
        map2 = [[(1 if i == 0 or j == 0 or i == width - 1 or j == height - 1 else 0) for i in range(width)] for j in range(height)]

        # helper function for neighbor grid generation
        def generate_neighbor(px,py,w,h):
            return [(i,j) for i in range(px-1,px+2) 
                    for j in range (py-1,py+2) 
                    if i>= 0 and j >= 0 and i < h and j < w]

        # a recursive function to illiminate all 0 that should be change to 1
        def infect_neighbor(m, point,w,h):
            neighbors = generate_neighbor(point[0],point[1],w,h)
            for i, j in neighbors:
                if m[i][j] == 0:
                    m[i][j] = 1
                    infect_neighbor(m, (i,j),w,h)

        # labelling the pipes
        for i in range(height):
            for j in range(width):

                if (i,j) in loop_lengths[0]:
                    map2[i][j] = 2

        # first stage of illimination
        for i in range(height):
            for j in range(width):
                
                if map2[i][j] == 1:
                    infect_neighbor(map2,(i,j),width,height)


        # expanding grid to handle special cases.
        map3 = [[0]*(3*width) for _ in range(3*height)]

        # further ellimination of squares
        for i in range(height):
            for j in range(width):
                if map2[i][j] == 1:
                    for x,y in generate_neighbor(i*3+1,j*3+1,width*3,height*3):
                        map3[x][y] = 1
                if map2[i][j] == 2:
                    map3[i*3+1][j*3+1] = 2
                    dir1 = map[i][j][0]
                    dir2 = map[i][j][1]
                    map3[i*3+1-dir1[0]][j*3+1-dir1[1]] = 2
                    map3[i*3+1-dir2[0]][j*3+1-dir2[1]] = 2
                    
        # tallying grid that's surrounded by the loop
        for i in range(height*3):
            for j in range(width*3):
                if map3[i][j] == 1:
                    infect_neighbor(map3,(i,j),width*3,height*3)

        counter_ = 0 
        for i in range(1,height*3,3):
            for j in range(1,width*3,3):
                if map3[i][j] == 0:
                    flag = True
                    for neighbor in generate_neighbor(i,j,width*3,height*3):
                        if map3[neighbor[0]][neighbor[1]] != 0:
                            flag = False
                            break
                    if flag:
                        counter_ += 1
        return (counter_)



if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = expanded_triangle_sum(input_file_path)
    end_time = time.time()  # Record the end time

    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The tile enclosed by the loops are {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
