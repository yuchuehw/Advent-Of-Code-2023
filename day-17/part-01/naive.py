"""
Advent of Code 2023 - Day 17, Part 1 (naive)

Task: Write a path finding algorithm to minimize heat loss!
"""

import time

DIRECTIONS = {(1,0):[(1,0),(0,1),(0,-1)],
              (-1,0):[(-1,0),(0,1),(0,-1)],
              (0,1):[(0,1),(1,0),(-1,0)],
              (0,-1):[(0,-1),(1,0),(-1,0)],
              None:[(0,1),(0,-1),(1,0),(-1,0)]
            }

def calculate_min_heat_lost(file_path: str) -> int:
    """
    Find the route with the lowest heat loss and return the sum of the heatloss.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - int: The sum of custom hash values.
    """
    with open(file_path, "r", encoding="utf8") as file:
        ht_lst_mp = []
        for line in file.readlines():
            ht_lst_mp.append([int(i) for i in list(line.strip())])

        # dict of points and most efficient way to get there and three most recent moves.
        mst_eff_rte = {(0,0):[0, [None, None, None]]}
        current_gen = [(0,0)]
        next_gen = []
        width = len(ht_lst_mp[0])
        height = len(ht_lst_mp)
        # conduct bfs on the heat map and run at most 10000 iterations before giving up.
        for _ in range(10000):
            # print(mst_eff_rte)
            # input()
            # print()
            print(f"gen{_}")
            for point in current_gen:
                # print(f"point({point})")
                prhbtd_dir = None
                # prhbtd_dir = (mst_eff_rte[point][1][0] 
                            # if mst_eff_rte[point][1][0]==mst_eff_rte[point][1][1]==mst_eff_rte[point][1][2] 
                            # else None)
                for dir in DIRECTIONS[mst_eff_rte[point][1][-1]]:
                    new_point = (point[0]+dir[0], point[1]+dir[1])
                    if prhbtd_dir != dir and 0 <= new_point[0] < height and 0 <= new_point[1] < width:
                        heat_lost_score = (mst_eff_rte[point][0] +
                                                ht_lst_mp[new_point[0]][new_point[1]])
                        new_most_recent_step = mst_eff_rte[point][1][1:]+[dir]
                        if new_point not in mst_eff_rte or heat_lost_score < mst_eff_rte[new_point][0]:
                            # print(new_point, heat_lost_score, new_most_recent_step)
                            mst_eff_rte[new_point] = [heat_lost_score, new_most_recent_step]
                            next_gen.append(new_point)
                            

            if len(next_gen) == 0:
                break
            else:
                current_gen = next_gen
                next_gen = []
        if (height-1,width-1) in  mst_eff_rte:
            return mst_eff_rte[(height-1,width-1)][0]
        else:
            return None


if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    input_file_path = "input.txt"
    result = calculate_min_heat_lost(input_file_path)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    print(f"The route with the least heat lost has a heat lost of {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
