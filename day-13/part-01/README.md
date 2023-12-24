# Advent of Code 2023 - Day 13, Part 1

## Task

Finding complete reflections and "summarize" them (sum of vert-symmmetry + sum of hori-symmetry * 100)

## Description

You note down the patterns of ash (.) and rocks (#) that you see as you walk (your puzzle input); perhaps by carefully analyzing these patterns, you can figure out where the mirrors are!

## Example

Consider the following example:

```
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
```

The above loop encloses merely four tiles. The middle tiles are not in the loop.

To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between two rows or across a vertical line between two columns.

In the first pattern, the reflection is across a vertical line between columns 5 and 6. The second pattern reflects across a horizontal line between rows 4 and 5.

To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to that, also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above example, the first pattern's vertical line has 5 columns to its left, and the second pattern's horizontal line has 4 rows above it, a total of 405.

Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all of your notes?

## Usage

```bash
python main.py
```

## Input

The input is read from a file named `input.txt`. The file should contain the puzzle patterns.

## Output

The script will output the sum of distances for all pairs.
