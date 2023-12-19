
# Advent of Code 2023 - Day 3, Part 2

This Python script is a solution for Day 3, Part 2 of Advent of Code 2023. It reads an engine schematic from a file, identifies gears (symbols `*` adjacent to exactly two part numbers), calculates the gear ratio for each gear, and sums up all the gear ratios.

## Prompt
The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:
```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```
In this schematic, there are two gears. The first is in the top left; it has part numbers `467` and `35`, so its gear ratio is `16345`. The second gear is in the lower right; its gear ratio is `451490`. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces `467835`.

What is the sum of all of the gear ratios in your engine schematic?

## Usage

1. Ensure you have a file named `input.txt` with the engine schematic.
2. Run the Python script:

   ```bash
   python solution.py
   ```

3. The script will output the sum of all gear ratios.

## Function Explanation

- The `sum_of_gear_ratio` function calculates the sum of all gear ratios in the engine schematic.

Feel free to explore and modify the code to suit your needs. Contributions and improvements are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
