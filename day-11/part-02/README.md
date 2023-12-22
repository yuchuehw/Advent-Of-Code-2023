# Advent of Code 2023 - Day 11, Part 1


## Prompt

Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with `1000000` empty rows, and each empty column should be replaced with `1000000` empty columns.

(In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)

Sure, I've made some improvements to your code to make it more readable and added a README.md file. Here's the updated code and the corresponding README.md:

## Task
Figure out the shortest distance of each pair of stars in an expanded universe.

## Input
The input file contains a grid representing galaxies and empty space after cosmic expansion.

Example:
```
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
```

## Approach
1. Read the input file and parse the galaxy map.
2. Identify empty rows and columns that expanded during cosmic expansion.
3. Calculate the shortest distance between each pair of stars, considering the expanded universe.
4. Sum up the lengths of all pairs to get the final result.

## How to Run
1. Set the `input_file_path` variable to the path of your input file.
2. Run the script.

## Example
For the given example input:

```
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
```
The sum of all star distances is calculated and printed.

## Output
The sum of the shortest distances between every pair of galaxies.

