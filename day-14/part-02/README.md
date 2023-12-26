# Advent of Code 2023 - Day 14, Part 2

## Prompt
The parabolic reflector dish deforms, but not in a way that focuses the beam. To do that, you'll need to move the rocks to the edges of the platform. Fortunately, a button on the side of the control panel labeled "spin cycle" attempts to do just that!

Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east. After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction. After one cycle, the platform will have finished rolling the rounded rocks in those four directions in that order.

Here's what happens in the example above after each of the first few cycles:

After 1 cycle:
```
.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....
```
After 2 cycles:
```
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#..OO###..
#.OOO#...O
```
After 3 cycles:
```
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
```
This process should work if you leave it running long enough, but you're still worried about the north support beams. To make sure they'll survive for a while, you need to calculate the total load on the north support beams after `1000000000` cycles.

In the above example, after `1000000000` cycles, the total load on the north support beams is `64`.

Run the spin cycle for `1000000000` cycles. Afterward, what is the total load on the north support beams?

## Task

2048 with stone (do 10000 cycles, each cycle consists of tilting to the first north, then west, then south, then east) and calculate torque.

## Approach
Since carrying out `1000000000` is quite time consuming. I write some code to detect if there's patterns in the cycle.(spoiler: there is). I therefore set up my code so that it would detect cycle and calculate the equivlent cycles.

## Description

The script `calculate_torque_after_cycles.py` simulates the movement of rounded rocks on a grid over 10000 cycles, where each cycle consists of tilting the platform to the north, west, south, and east. The goal is to calculate the total torque on the north support beams after these cycles.

## Solution

The script uses the `tilt_to_direction` function to tilt the grid in the specified direction (north, west, south, east). The `cycle` function performs a full cycle by tilting the platform in all four directions. The main function, `calculate_torque_after_cycles`, reads the input grid from a file, simulates the cycles, and calculates the total torque on the north support beams. It also handles cases where the cycle patterns start repeating.

## Usage

```bash
python main.py
```

## Input

The input is read from a file named `input.txt`. The file should contain the arrangement of rocks and empty spaces on the platform.

## Output

The script will output the total torque on the north support beams after simulating 10000 cycles.
