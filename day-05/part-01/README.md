# Advent of Code 2023 - Day 5, Part 1

## Prompt
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48

The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51

With this map, you can look up the soil number required for each initial seed number:

  Seed number 79 corresponds to soil number 81.
  Seed number 14 corresponds to soil number 14.
  Seed number 55 corresponds to soil number 57.
  Seed number 13 corresponds to soil number 13.

The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

  Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location `82`.
  Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location `43`.
  Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location `86`.
  Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location `35`.

So, the lowest location number in this example is `35`.

What is the lowest location number that corresponds to any of the initial seed numbers?


## Task Description
Using the crazy lookup table to find the seed with the smallest location number.

## Instructions
1. Ensure you have the correct Python interpreter installed.
2. Run the script using the provided input file.
3. The script will calculate and display the minimum location number corresponding to any of the initial seed numbers.

## Usage
```bash
python main.py
```

## Input Format
The input file should contain information about seeds and conversion maps.

## Output Format
The script will output the minimum location number.

```plaintext
The min location is: [result]
```
