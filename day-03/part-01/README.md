# Advent of Code 2023 - Day 3, Part 1

This Python script is a solution for Day 3, Part 1 of Advent of Code 2023. It reads an engine schematic from a file and calculates the sum of all numbers (engine parts) that are adjacent to at least one symbol. A dot-symbol (.) is not considered a symbol in this exercise.

## Prompt
The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: `114` (top right) and `58` (middle right). `Every other number is adjacent` to a symbol and so is a part number; their sum is `4361`.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

## Usage

1. Ensure you have a file named `input.txt` with the engine schematic.
2. Run the Python script:

   ```bash
   python main.py
   ```

3. The script will output the sum of all engine parts.

## Function Explanation

- The `sum_of_engine_part` function calculates the sum of all numbers (engine parts) that are adjacent to at least one symbol.

Feel free to explore and modify the code to suit your needs. Contributions and improvements are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
