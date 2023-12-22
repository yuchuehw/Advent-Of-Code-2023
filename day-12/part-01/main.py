"""
Advent of Code 2023 - Day 12, Part 1

Task: Find all configurations/permutations of fountains given the data.
"""

import time

# Status of the spring. Convert chr to int.
STATUS = {".": 0, "#": 1, "?": 2}

def finisher(sequence, counter, record):
    """
    Check if the given sequence satisfies the finishing conditions.

    Args:
        seq (list): List representing the sequence of springs.
        counter (int): Counter variable for tracking the current position in the sequence.
        record (list): List representing the record of broken spring groups.

    Returns:
        bool: True if the sequence satisfies the finishing conditions, False otherwise.
    """
    record_index = 0
    for fountain in sequence:
        if counter == 0:
            if fountain == 0:
                pass
            elif fountain == 1:
                counter = 1
            else:
                raise Exception("PANIC")
        else:
            if fountain == 0:
                if counter == record[record_index]:
                    counter = 0
                    record_index += 1
                else:
                    return 0
            if fountain == 1:
                if counter < record[record_index]:
                    counter += 1
                else:
                    return 0

    return 1

def search_next_node(sequence, next, brk, nonbrk, counter, record):
    """
    Binary search function that looks through all nodes.

    Args:
        seq (list): List representing the sequence of springs.
        next_ (bool): True if searching for the next broken spring, False otherwise.
        brk (int): Count of remaining broken springs.
        nonbrk (int): Count of remaining non-broken springs.
        counter (int): Counter variable for tracking the current position in the sequence.
        record (list): List representing the record of broken spring groups.

    Returns:
        int: The number of possible arrangements.
    """
    if not counter:
        if not sequence:
            return 1
        if sequence[0] == 0:
            return search_next_node(sequence[1:], next, brk, nonbrk, 0, record)
        elif sequence[0] == 1:
            return search_next_node(sequence[1:], next, brk, nonbrk, 1, record)
        elif sequence[0] == 2 and not next:
            if brk == 0 and nonbrk - 1 == 0:
                return finisher(sequence[1:], 0, record)
            return (search_next_node(sequence[1:], True, brk, nonbrk-1, 0, record) if brk else 0) + \
                   (search_next_node(sequence[1:], False, brk, nonbrk-1, 0, record) if nonbrk-1 else 0)
        elif sequence[0] == 2:
            if brk - 1 == 0 and nonbrk == 0:
                return finisher(sequence[1:], 1, record)
            return (search_next_node(sequence[1:], True, brk-1, nonbrk, 1, record) if brk-1 else 0) + \
                   (search_next_node(sequence[1:], False, brk-1, nonbrk, 1, record) if nonbrk else 0)
        else:
            raise Exception("PANIC")
    else:
        if not sequence:
            return 1
        if sequence[0] == 0 and counter == record[0]:
            return search_next_node(sequence[1:], next, brk, nonbrk, 0, record[1:])
        elif sequence[0] == 0:
            return 0
        elif sequence[0] == 1 and counter < record[0]:
            return search_next_node(sequence[1:], next, brk, nonbrk, counter+1, record)
        elif sequence[0] == 1:
            return 0
        elif sequence[0] == 2 and not next and counter == record[0]:
            if brk == 0 and nonbrk - 1 == 0:
                return finisher(sequence[1:], 0, record[1:])
            return (search_next_node(sequence[1:], True, brk, nonbrk-1, 0, record[1:]) if brk else 0) + \
                   (search_next_node(sequence[1:], False, brk, nonbrk-1, 0, record[1:]) if nonbrk-1 else 0)
        elif sequence[0] == 2 and not next:
            return 0
        elif sequence[0] == 2 and next and counter < record[0]:
            if brk - 1 == 0 and nonbrk == 0:
                return finisher(sequence[1:], counter+1, record)
            return (search_next_node(sequence[1:], True, brk-1, nonbrk, counter+1, record) if brk-1 else 0) + \
                   (search_next_node(sequence[1:], False, brk-1, nonbrk, counter+1, record) if nonbrk else 0)
        elif sequence[0] == 2 and next:
            return 0
        else:
            raise Exception("PANIC")

def possible_fountain_config(file_path):
    """
    Count all the different arrangements of operational and broken springs that meet the given criteria for each row.

    Args:
        file_path (str): The path to the input file.

    Returns:
        int: The sum of all possible arrangements.
    """
    with open(file_path, "r", encoding="utf8") as file:
        total_sum = 0
        for line in file.readlines():
            springs, record = line.strip().split(" ")
            springs = [STATUS[ch] for ch in springs]
            record = [int(num) for num in record.split(",")]

            total_unknown = springs.count(2)
            broken_unknown_count = sum(record) - springs.count(1)
            nonbrkn_unknown_count = total_unknown - broken_unknown_count

            if broken_unknown_count != 0 and nonbrkn_unknown_count != 0:
                s1 = search_next_node(springs, True, broken_unknown_count, nonbrkn_unknown_count, 0, record)
                s2 = search_next_node(springs, False, broken_unknown_count, nonbrkn_unknown_count, 0, record)
                total_sum += (s1 + s2)
            else:
                total_sum += 1

        return total_sum

if __name__ == "__main__":
    start_time = time.time()
    input_file_path = "input.txt"
    result = possible_fountain_config(input_file_path)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"The sum of all possible combination config is {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
