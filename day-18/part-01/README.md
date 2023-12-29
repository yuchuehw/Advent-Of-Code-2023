# Advent of Code 2023 - Day 18, Part 1

## Problem Statement

This task involves drawing a map by following a set of directions and then calculating the area bounded by the map.

### Approach

The script employs a numpy array to efficiently represent the map and dynamically resizes it as needed. It then follows the given directions, updating the map accordingly. Finally, the outermost layer of the map is considered to calculate the area.


### Description

The `main.py` script reads a set of directions from an input file and draws a map based on those directions. The script uses a numpy array to represent the map, dynamically resizing it as needed. The area bounded by the map is then calculated by considering the outermost layer of the map.

### Usage

```bash
python main.py
```

### Input

The input is read from a file named `input.txt`. Each line of the file contains a direction ("R", "L", "D", or "U") and the number of steps to move in that direction.

Example input file:
```
R 5
U 3
L 2
D 4
```

### Output

The script will output the calculated area of the map, considering the boundaries formed by the drawn directions.

