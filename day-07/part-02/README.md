# Advent of Code 2023 - Day 7, Part 2

## Prompt

To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

Now, the above example goes very differently:

```
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
```

  - 32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
  - KK677 is now the only two pair, making it the second-weakest hand.
  - T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.

With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?


## Task
Determine how much you win in a poker-like game with the given list of hands and bets, where J is a joker and can replace any other card.

## Input
The input file contains hands and their corresponding bid amounts.

Example:
```
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
```

## Approach
1. Read race data from the input file, extracting each hand and its corresponding bid amount.
2. Determine the strength of each hand based on the rules provided.
3. Sort the hands in descending order of strength and bid amounts to get the final ranking.
4. Calculate the total winnings by multiplying each hand's bid with its rank.
5. Return the total winnings.

## How to Run
1. Set the `input_file_path` variable to the path of your input file.
2. Run the script.

## Example
For the given example:
```
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
```
The total winnings are calculated and printed.

## Output
The total winnings in the poker-like game with J as a joker.
