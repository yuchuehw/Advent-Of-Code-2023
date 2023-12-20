"""
Advent of Code 2023 - Day 6, Part 1

Task: Determine the number of ways you can win each race (number of integer seconds you can hold the button) to win the race given the provided data.

actual ignore the space hehehehe

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
        race_duration = int(race_duration[race_duration.index(":")+1:].replace(" ",""))
        distance_to_beat = int(distance_to_beat[distance_to_beat.index(":")+1:]
                               .replace(" ",""))
        # print([(race_duration, distance_to_beat)])
        return [(race_duration, distance_to_beat)]


def calc_possibility_product(race_data: list) -> int:
    """
    Calculate the product of the ways to win in the single race.

    Args:
        race_data (list): List of tuples containing race duration and distance to beat.

    Returns:
        int: The product of ways to win in the single race.
    """
    product_ = 1
    for race_duration, distance_to_beat in race_data:

        start = 0
        end = 0
        
        for time in range(race_duration+1):
            if time*(race_duration-time) > distance_to_beat:
                start = time
                break

        for time in range(race_duration,-1,-1):
            if time*(race_duration-time) > distance_to_beat:
                end = time
                break
                
        product_*= (end-start+1)
    return product_
    
if __name__ == "__main__":
    input_file_path = "input.txt"
    race_data = read_race_data(input_file_path)
    result = calc_possibility_product(race_data)
    print(f"The number of ways to win the race is {result}")
