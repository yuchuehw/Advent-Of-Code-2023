# Advent of Code 2023 - Day 1, Part 2

This Python script is a solution for Day 1, Part 2 of Advent of Code 2023. It reads a file containing lines of text and calculates the sum of calibration values based on the first and last digits. The digits can be either numeric or spelled out.

## Prompt
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:
```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```
In this example, the calibration values are `29`, `83`, `13`, `24`, `42`, `14`, and `76`. Adding these together produces `281`.

What is the sum of all of the calibration values?


## Usage

1. Ensure you have a file named `input.txt` with the calibration document.
2. Run the Python script:

   ```bash
   python main.py
   ```

3. The script will output the sum of calibration values.

## Function Explanation

- The `calculate_calibration_sum` function takes a file path as an argument and returns the sum of calibration values.
- The script uses dictionaries to represent numeric and spelled-out digits for better readability and flexibility.
- Candidate locations for both types of digits are collected and processed to find the first and last digits for each line.
- The sum of these two-digit numbers is then returned as the result.

Feel free to explore and modify the code to suit your needs. Contributions and improvements are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
