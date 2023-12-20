"""
Advent of Code 2023 - Day 7, Part 1

Task: Determine how much do you win in a poker like game! You are provided with a list of hands and bets!

"""
from collections import Counter


# 250085923 too small
# 250346234 too big

# from the smallest to biggest
CARD_STRENGTH = {"2":2,
                 "3":3,
                 "4":4,
                 "5":5,
                 "6":6,
                 "7":7,
                 "8":8,
                 "9":9,
                 "T":10,
                 "J":11,
                 "Q":12,
                 "K":13,
                 "A":14
                }

# from smallest to biggest
HAND_STRENGTH = {(1,1,1,1,1):1, # high card
                 (1,1,1,2):2, # one pair
                 (1,2,2):3, # two pair
                 (1,1,3):4, # three of a kind
                 (2,3):5, # full house
                 (1,4):6, # four of a kind
                 (5,):7} # five of a kind

def get_bet_win(file_path: str) -> int:
    """
    Read race data from the input file.

    Args:
        file_path (str): The path to the input file.

    Returns:
        int: A tallied total win with the multiple.
    """
    with open(file_path, "r", encoding="utf8") as file:
        l = []
        for line in file.readlines():
            hand, bid = line.strip().split(" ")
            counted_hand = Counter(hand)
            hand_strength = HAND_STRENGTH[tuple(sorted(counted_hand.values()))]

            l.append((hand_strength, 
                      tuple([CARD_STRENGTH[c] for c in hand]), bid))
            
            # I didn't read the question clear enought. this is not 
            # normal poker and you do not re-order cards from biggest 
            # to smallest
            # order = [CARD_STRENGTH[_[0]] for _ in 
            #          sorted(counted_hand.items(), 
            #                 key= lambda _: (-_[1],-CARD_STRENGTH[_[0]]))] 
            
            # l.append((hand_strength,order, "".join(sorted(hand)), bid))

        

        # print(*sorted(l),sep="\n")
        
        total_win = 0
        for i,bet_tuple in enumerate(sorted(l)):
            *_, bid = bet_tuple
            # print(i)
            ot = total_win
            total_win += int(bid)*(i+1)
            # print(f"{ot}+{int(bid)*(i+1)}={total_win}")
        return total_win


if __name__ == "__main__":
    input_file_path = "input4.txt"
    result = get_bet_win(input_file_path)
    print(f"you win {result}")
