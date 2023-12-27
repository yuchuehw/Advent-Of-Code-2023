
# Advent of Code 2023 - Day 16, Part 1

## Task

Ray tracing! Determine how many squares will be energized by the beam.

## Description

The script `main.py` implements ray tracing to determine the number of squares energized by a beam. The input map is read from a file, and the script recursively energizes squares based on specified rules and directions. The energized squares are marked in an energize map, and the total number of energized squares is calculated.

## Solution

The script uses recursion to navigate the map and energize squares based on certain conditions. It maintains an energize map to keep track of energized squares and avoids revisiting coordinates using a set. The total sum of energized squares is then computed.

## Analysis
The progam is very straightforward. The beam would recursively find the next square it would end up in and end only if it return to a square that is already visited or it hit the wall(go out of bound). The diagonal mirror can be though of changing x direction to y (and flippping the sign).

## Usage

```bash
python main.py
```

## Input

The input is read from a file named `input.txt`. The file should contain a map representing the beam directions.

Example input file:
```
#######-
#/#/\\/-  <- Example representation of the beam
#/#/\\--
\\#\\/#/-
\\\\\\/#/
#-\\\-/\\
#///\\\\
--/\\\\\
```

## Output

The script will output the sum of energized squares.
