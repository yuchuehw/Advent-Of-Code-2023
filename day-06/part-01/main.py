"""
Advent of Code 2023 - Day 6, Part 1

Task: Determine the number of ways you can win each race (number of integer seconds you can hold the button) to win the race given the provided data.
"""

def read_race_data(file_path: str) -> list:
    """
    Read race data from the input file.

    Args:
        file_path (str): The path to the input file.

    Returns:
        list: List of tuples containing race duration and distance to beat.
    """
    with open(file_path, "r", encoding="utf8") as file:
        race_duration, distance_to_beat = file.read().split("\n")
        race_duration = [int(num) for num in race_duration.split() if num.isnumeric()]
        distance_to_beat = [int(num) for num in distance_to_beat.split() if num.isnumeric()]
        return list(zip(race_duration, distance_to_beat, strict=True))


def calc_possibility_product(race_data: list) -> int:
    """
    Calculate the product of the ways to win in all races.

    Args:
        race_data (list): List of tuples containing race duration and distance to beat.

    Returns:
        int: The product of ways to win in all races.
    """
    product_ = 1
    for race_duration, distance_to_beat in race_data:
        ways_of_winning = sum(1 for time in range(race_duration + 1) if time * (race_duration - time) > distance_to_beat)
        product_ *= ways_of_winning

    return product_

if __name__ == "__main__":
    input_file_path = "input4.txt"
    race_data = read_race_data(input_file_path)
    result = calc_possibility_product(race_data)
    print(f"The product of ways to win in all races is {result}")
