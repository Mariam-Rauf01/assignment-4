import random  # Import the random module to generate random numbers

def main():
    # Generate the secret number at random between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get the user's initial guess
    guess = int(input("Enter a guess: "))
    
    # Loop until the user guesses the correct number
    while guess != secret_number:
        if guess < secret_number:  # If the guess is less than the secret number
            print("Your guess is too low")
        else:  # If the guess is greater than the secret number
            print("Your guess is too high")
        
        print()  # Print an empty line for better readability
        guess = int(input("Enter a new guess: "))  # Prompt for a new guess
    
    # Congratulate the user when they guess correctly
    print("Congrats! The number was: " + str(secret_number))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function