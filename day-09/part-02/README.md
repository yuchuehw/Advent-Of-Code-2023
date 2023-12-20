
## Day 9 - Part 2

## Prompt

Of course, it would be nice to have even more history included in your report. Surely it's safe to just extrapolate backwards as well, right?

For each history, repeat the process of finding differences until the sequence of differences is entirely zero. Then, rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

In particular, here is what the third example history looks like when extrapolating back in time:
```
5  10  13  16  21  30  45
  5   3   3   5   9  15
   -2   0   2   4   6
      2   2   2   2
        0   0   0
```
Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most history value: `5`.

Doing this for the remaining example data above results in previous values of `-3` for the first history and `0` for the second history. Adding all three new values together produces `2`.

Analyze your OASIS report again, this time extrapolating the previous value for each history. What is the sum of these extrapolated values?


## Problem breakdown
In Advent of Code 2023 - Day 9, Part 2, the task is to solve a problem related to a Gaussian triangle. In addition to predicting the next value, the challenge now involves finding the value that would have come before the very first value and summing up all these previous values for all triangles.

## Instructions:

1. **Run the Code:**
   ```bash
   python main.py
   ```

   This will display the sum of extrapolated previous values for each triangle based on the provided input.

## Input:

The input is read from a file named `input.txt`. Ensure that this file contains the necessary data following the specified format.

## Output:

The output will be the sum of extrapolated previous values for all triangles.
