    """
    Advent of Code 2023 - Day 1, Part 1

    Task: Read a file and return the sum of digits made up by each line.
    The number made by each line is defined to be the first digit multiplied by ten and added with the last digit.
    """

    NUMBERS = {str(i): i for i in range(10)}

    def calculate_calibration_sum(file_path):
        """
        Calculate the sum of calibration values based on the given file.

        Args:
            file_path (str): The path to the input file.

        Returns:
            int: The sum of calibration values.
        """
        total_sum = 0

        with open(file_path, "r", encoding="utf8") as file:
            for line in file.readlines():
                for char in line:
                    if char in NUMBERS:
                        total_sum += NUMBERS[char] * 10
                        break

                for char in reversed(line):
                    if char in NUMBERS:
                        total_sum += NUMBERS[char]
                        break

        return total_sum

    if __name__ == "__main__":
        input_file_path = "input.txt"
        result = calculate_calibration_sum(input_file_path)
        print(f"The sum of calibration values is: {result}")
