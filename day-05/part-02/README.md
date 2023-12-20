# Advent of Code 2023 - Day 5, Part 1

## Prompt

Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the `start of the range` and the second value is the `length of the range`. So, in the first line of the example above:

seeds: `79 14 55 13`

This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number `79` and contains `14` values: `79, 80, ..., 91, 92`. The second range starts with seed number `55` and contains `13` values: `55, 56, ..., 66, 67`.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is `46`.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?


## Problem Description

Given a crazy lookup table and a list of initial seed numbers, find the seed with the smallest corresponding location number. The seeds are provided in start, range pairs.

## Solution

The solution involves a lookup function that performs conversions using a translation table. The data is organized from the input file, and the minimum location number is found after multiple conversions.

## Usage

1. Replace the contents of `input.txt` with your input data.
2. Run the script using `python main.py`.
3. The minimum location number will be printed.

## Functions

### `lookup`

Performs a lookup using the translation table to convert from one category to another.

### `reorganize_data`

Reads the input file and organizes the data into seed pairs and a translation table.

### `find_min_via_steps`

Finds the minimum location number corresponding to the initial seeds after multiple conversions.

