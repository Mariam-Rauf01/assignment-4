"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times. Prints
the results of each die roll. This program is used
to show how variable scope works.
"""

import random

NUM_SIDES = 6  # Constant for the number of sides on the dice

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)  # Roll the first die
    die2 = random.randint(1, NUM_SIDES)  # Roll the second die
    total = die1 + die2  # Calculate the total of both dice
    print(f"Die 1: {die1}, Die 2: {die2} → Total: {total}")  # Print the results

def main():
    die1 = 10  # Local variable in main()
    print(f"die1 in main() starts as: {die1}")  # Print the initial value of die1

    for _ in range(3):  # Loop to roll the dice three times
        roll_dice()  # Call the roll_dice function

    print(f"die1 in main() is still: {die1}")  # Print the value of die1 after rolling

if __name__ == '__main__':
    main()  # Execute the main function