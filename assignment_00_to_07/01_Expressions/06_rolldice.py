import random

# Function to roll two dice
def roll_dice():
    die1 = random.randint(1, 6)  # Roll the first die
    die2 = random.randint(1, 6)  # Roll the second die
    return die1, die2

# Main program
while True:
    # Prompt the user to roll the dice or exit
    user_input = input("Press 'r' to roll the dice or 'exit' to quit: ")
    
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    elif user_input.lower() == 'r':
        # Roll the dice
        die1, die2 = roll_dice()
        
        # Calculate the total
        total = die1 + die2
        
        # Print the results
        print(f"You rolled a {die1} and a {die2}.")
        print(f"The total is: {total}\n")
    else:
        print("Invalid input. Please press 'r' to roll the dice or 'exit' to quit.")