# Advent of Code 2023 - Day 8, Part 1

## Prompt
One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of network of labeled nodes.

It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!

After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.

This format defines each node of the network individually. For example:
```
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
```
Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in `2` steps.

Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes `6` steps to reach ZZZ:
```
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
```
Starting at `AAA`, follow the left/right instructions. How many steps are required to reach `ZZZ`?

## Problem Description

Given a network of labeled nodes and left/right instructions, determine the number of steps required to get from a starting point (AAA) to a destination point (ZZZ).

## Solution

The solution involves reading the input file, organizing the network, and following left/right instructions until the destination point is reached.

## Usage

1. Replace the contents of `input.txt` with your input data.
2. Run the script using `python script_name.py`.
3. The number of steps required to reach the destination point will be printed.

## Functions

### `plan_route`

Reads the input file, organizes the network, and determines the number of steps required to get from the starting point to the destination point.

## Input Format

The input file should contain left/right instructions and a description of the network of labeled nodes.

## Example

```python
input_file_path = "input.txt"
steps = plan_route(input_file_path, "AAA", "ZZZ")
print(f"According to the map, it takes {steps} steps to get from AAA to ZZZ")
```
