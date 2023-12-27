# Advent of Code 2023 - Day 17, Part 1

## Problem Statement

The task is to find the route with the least heat loss through a given map. Each cell in the map has a specific heat loss value, and the route must minimize the total heat loss from the starting point to the bottom-right corner.

## `main.py`

### Description

The `main.py` script uses a priority queue (heap) and a modified version of Dijkstra's algorithm to efficiently explore possible routes while minimizing heat loss. It considers consecutive moves in the same direction and avoids revisiting points with the same direction to prevent unnecessary exploration.

### Usage

```bash
python main.py
```

### Input

The input is read from a file named `input.txt`. The file should contain a map of heat loss values, where each cell represents the heat loss at that position.

Example input file:
```
2310
1341
1521
0254
1513
```

### Output

The script will output the heat loss of the route with the least heat loss.

## `naive.py`

### Description

The `naive.py` script represents the initial solution to the problem. It uses BFS instead of Dijkstra's Algorithm. It worked well for smaller grid but way longer to run for bigger grid.

```bash
python naive.py
```


### Input

The input is read from a file named `input.txt` similar to the `main.py` script.

### Output

The script will output the heat loss of the route with the least heat loss.

### Performance Comparison

The `main.py` script provides a more efficient solution by using a heuristic-based approach and avoiding unnecessary exploration. It is significantly faster than the approach employed by `naive.py`, especially for larger maps.
