
# Advent of Code 2023 - Day 13, Part 2

## Prompt
You resume walking through the valley of mirrors and - SMACK! - run directly into one. Hopefully nobody was watching, because that must have been pretty embarrassing.

Upon closer inspection, you discover that every mirror has exactly one smudge: exactly one . or # should be the opposite type.

In each pattern, you'll need to locate and fix the smudge that causes a different reflection line to be valid. (The old reflection line won't necessarily continue being valid after the smudge is fixed.)

Here's the above example again:
```
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
```
```
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
```
The first pattern's smudge is in the top-left corner. If the top-left # were instead ., it would have a different, horizontal line of reflection:
```
1 ..##..##. 1
2 ..#.##.#. 2
3v##......#v3
4^##......#^4
5 ..#.##.#. 5
6 ..##..##. 6
7 #.#.##.#. 7
```
With the smudge in the top-left corner repaired, a new horizontal line of reflection between rows 3 and 4 now exists. Row 7 has no corresponding reflected row and can be ignored, but every other row matches exactly: row 1 matches row 6, row 2 matches row 5, and row 3 matches row 4.

In the second pattern, the smudge can be fixed by changing the fifth symbol on row 2 from . to #:
```
1v#...##..#v1
2^#...##..#^2
3 ..##..### 3
4 #####.##. 4
5 #####.##. 5
6 ..##..### 6
7 #....#..# 7
```
Now, the pattern has a different horizontal line of reflection between rows 1 and 2.

Summarize your notes as before, but instead use the new different reflection lines. In this example, the first pattern's new horizontal line has `3` rows above it and the second pattern's new horizontal line has `1` row above it, summarizing to the value `400`.

In each pattern, fix the smudge and find the different line of reflection. What number do you get after summarizing the new reflection line in each pattern in your notes?


## Task

First fix symmetry then "summarize" them (sum of vert-symmetry + sum of hori-symmetry * 100)

## Description

You resume walking through the valley of mirrors and - SMACK! - run directly into one. Hopefully, nobody was watching, because that must have been pretty embarrassing.

Upon closer inspection, you discover that every mirror has exactly one smudge: exactly one . or # should be the opposite type.

In each pattern, you'll need to locate and fix the smudge that causes a different reflection line to be valid. (The old reflection line won't necessarily continue being valid after the smudge is fixed.)

Summarize your notes as before, but instead use the new different reflection lines. In each pattern, fix the smudge and find the different line of reflection. What number do you get after summarizing the new reflection line in each pattern in your notes?

## Implementation
Instead of using map of string we can use `0` and `1` to represent the `.` and `#`. The problem specifically says that one of the cell is incorrect. We can thus implement an algorithm to check for almost complete symmetry by checking if the symmetry's absolute difference in the symmetric rows are exactly 1.

## Usage

```bash
python main.py
```

## Input

The input is read from a file named `input.txt`. The file should contain the puzzle patterns.

## Output

The script will output the sum of distances for all pairs.
