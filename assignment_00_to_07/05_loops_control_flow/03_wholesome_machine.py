AFFIRMATION: str = "I am capable of doing anything I put my mind to."  # The affirmation to be typed

def main():
    # Prompt the user to type the affirmation
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  # Get user's input
    # Loop until the user types the correct affirmation
    while user_feedback != AFFIRMATION:
        # Inform the user that their input was incorrect
        print("That was not the affirmation.")

        # Prompt the user to type the affirmation again
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()  # Get the new input from the user

    # Inform the user that they typed the affirmation correctly
    print("That's right! :)")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function