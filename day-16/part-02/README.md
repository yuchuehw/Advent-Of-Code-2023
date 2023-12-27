# Advent of Code 2023 - Day 16, Part 2

## Task

Ray tracing! Determine how many squares will be energized by the beam, considering all possible starting positions.

## Description

The script `main.py` extends the ray tracing algorithm to consider all possible starting positions along the edges of the map. The goal is to determine the maximum sum of energized squares by exploring various starting points and directions.

## Analysis

There's not much I added to the code from part1. I write a loop to test out every cell on the edge of the map and then find the one that energize the most cell. Brute force? Kinda. It only took 10ish second so I am too lasy to optimize further.

## Solution

The script uses recursion to navigate the map and energize squares based on certain conditions. It maintains an energize map to keep track of energized squares and avoids revisiting coordinates using a set. The script explores starting positions from the top, bottom, left, and right edges of the map and calculates the sum of energized squares for each possibility. The final result is the maximum sum among all possibilities.

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

The script will output the maximum sum of energized squares considering all possible starting positions.
