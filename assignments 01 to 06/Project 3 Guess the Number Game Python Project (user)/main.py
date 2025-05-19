def guess_the_number():
    print("===================================")
    print("      Guess the Number Game       ")
    print("===================================")
    print("Think of a number between 1 and 100, and I will try to guess it.")

    low = 1
    high = 100
    attempts = 0
    guessed = False

    while not guessed:
        # Computer makes a guess
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")

        # Get user feedback
        feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").strip().upper()

        if feedback == 'C':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
            guessed = True
        elif feedback == 'H':
            high = guess - 1
            print("Okay, I'll guess lower.")
        elif feedback == 'L':
            low = guess + 1
            print("Okay, I'll guess higher.")
        else:
            print("Invalid input. Please enter H, L, or C.")

if __name__ == "__main__":
    guess_the_number()