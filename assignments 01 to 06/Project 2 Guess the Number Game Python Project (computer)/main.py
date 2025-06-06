import random

def guess_the_number():
    print("===================================")
    print("      Guess the Number Game       ")
    print("===================================")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            # Get user input
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess_the_number()