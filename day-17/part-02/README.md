# Advent of Code 2023 - Day 17, Part 2

## Problem Statement

This task builds upon the previous part (Day 17, Part 1) and extends it to consider a variation where consecutive moves in the same direction have a limit. The goal remains to find the route with the least heat loss through a given map.

## `main.py`

### Description

The `main.py` script introduces a modified version of the path-finding algorithm to minimize heat loss. The modification involves limiting consecutive moves in the same direction to 10, and only considering those directions that meet this criterion. The script uses a priority queue (heap) to efficiently explore possible routes.

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

The script will output the heat loss of the route with the least heat loss, considering the modified consecutive moves limit.

### Performance

The script efficiently explores possible routes using a priority queue and limits consecutive moves, making it more optimized than the original path-finding algorithm. This approach significantly improves performance, especially for larger maps. The run time for my particular input took approximately 30 seconds.
