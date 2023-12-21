# Advent of Code 2023 - Day 10, Part 1

## Prompt
You find yourself in a field densely packed with pipes, all arranged in a two-dimensional grid of tiles. Your task is to discover the single large, continuous loop of pipes starting at the initial position 'S'. Determine the number of steps along the loop it takes to reach the point farthest from the starting position.

The pipes are represented using the following symbols:

- `|`: Vertical pipe connecting north and south.
- `-`: Horizontal pipe connecting east and west.
- `L`: 90-degree bend connecting north and east.
- `J`: 90-degree bend connecting north and west.
- `7`: 90-degree bend connecting south and west.
- `F`: 90-degree bend connecting south and east.
- `.`: Ground; no pipe in this tile.
- `S`: Starting position of the animal; there is a pipe on this tile.

Every pipe in the main loop connects to its two neighbors, and S connects to exactly two pipes. The goal is to find the tile in the loop that is farthest from the starting position in terms of the number of steps along the loop.

## Task
Find the single giant loop starting at 'S'. Determine how many steps along the loop it takes to get from the starting position to the point farthest from the starting position.

## Input
The input file contains a grid of tiles representing the field.

Example:
```
.....
.F-7.
.|.|.
.L-J.
.....
```

## Approach
1. Read the field data from the input file, creating a map of pipes.
2. Identify the starting point 'S' in the map.
3. Traverse the loop, calculating the distance from the starting position for each tile in the loop.
4. Determine the farthest point from the starting position in terms of the number of steps along the loop.
5. Return the number of steps.

## How to Run
1. Set the `input_file_path` variable to the path of your input file.
2. Run the script.

## Example
For the given example:
```
.....
.F-7.
.|.|.
.L-J.
.....
```
The number of steps along the loop to the farthest point is calculated and printed.

## Output
The number of steps along the loop to the farthest point from the starting position.
