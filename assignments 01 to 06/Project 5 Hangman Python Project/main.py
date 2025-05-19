import random
import string
import time  # <-- Importing time module

def get_random_word():
    words = ['python', 'hangman', 'programming', 'challenge', 'development', 'computer', 'science', 'artificial', 'intelligence', 'algorithm']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """
    ]
    return stages[6 - tries]

def print_heading():
    print("\n" + "=" * 35)
    print("         WELCOME TO HANGMAN")
    print("=" * 35 + "\n")

# Game Start
print_heading()
start_time = time.time()  # Start timer

word = get_random_word()
word_letters = set(word)
guessed_letters = set()
tries = 6
game_over = False

while not game_over:
    print(display_hangman(tries))
    print("Word: ", ' '.join([letter if letter in guessed_letters else '_' for letter in word]))
    print("Guessed Letters: ", ' '.join(sorted(guessed_letters)))

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or guess not in string.ascii_lowercase:
        print("Invalid input. Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        word_letters.remove(guess)
        print("Good guess!")
    else:
        tries -= 1
        print("Wrong guess. You lose a try.")

    if len(word_letters) == 0:
        elapsed_time = int(time.time() - start_time)
        print(f"\n🎉 Congratulations! You guessed the word: '{word}'")
        print(f"⏱️ Time taken: {elapsed_time} seconds")
        game_over = True
    elif tries == 0:
        elapsed_time = int(time.time() - start_time)
        print(display_hangman(tries))
        print(f"\n💀 Game Over! The word was: '{word}'")
        print(f"⏱️ Time taken: {elapsed_time} seconds")
        game_over = True


