# Advent of Code 2023 - Day 6, Part 2

## Prompt

--- Part Two ---

As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

So, the example from before:

```
Time:      7  15   30
Distance:  9  40  200
```
...now instead means this:

```
Time:      71530
Distance:  940200
```

Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

How many ways can you beat the record in this one much longer race?


## Task Description
Determine the number of ways you can win the single race given the provided data.

## Code Overview
- `read_race_data(file_path: str) -> list`: Reads race data from the input file.
- `calc_possibility_product(race_data: list) -> int`: Calculates the product of the ways to win in the single race.

## Instructions
1. Ensure you have Python installed on your machine.
2. Clone this repository.
   ```bash
   git clone <repository-url>
   ```
3. Navigate to the directory containing the code.
   ```bash
   cd <repository-directory>
   ```
4. Execute the script by providing the input file path.
   ```bash
   python script.py input.txt
   ```
   Replace `input.txt` with the path to your input file.

## Example
```bash
python main.py
```

## Input Format
The input file should contain a single line with race time and record distance, without spaces between numbers.

Example:
```
Time: 71 53 0
Distance: 94 12 90
```

## Output
The script will print the number of ways to win the single race. Ignoreing all the spaces

