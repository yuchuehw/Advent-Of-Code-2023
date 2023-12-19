
# Advent of Code 2023 - Day 1, Part 1

This Python script is a solution for Day 1, Part 1 of Advent of Code 2023. It reads a file containing lines of text and calculates the sum of calibration values based on the first and last digits of each line.

## Prompt
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```

In this example, the calibration values of these four lines are `12`, `38`, `15`, and `77`. Adding these together produces `142`.

Consider your entire calibration document. What is the sum of all of the calibration values?


## Usage

1. Ensure you have a file named `input.txt` with the calibration document.
2. Run the Python script:

   ```bash
   python main.py
   ```

3. The script will output the sum of calibration values.

## Function Explanation

- The `calculate_calibration_sum` function takes a file path as an argument and returns the sum of calibration values.
- It reads each line from the file, extracts the first and last digits, and calculates the corresponding two-digit number.
- The sum of these two-digit numbers is then returned as the result.

Feel free to explore and modify the code to suit your needs. Contributions and improvements are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
