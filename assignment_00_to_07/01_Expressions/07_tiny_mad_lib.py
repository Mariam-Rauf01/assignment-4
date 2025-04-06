# Define ANSI escape codes for bold and italic
BOLD_ITALIC = "\033[1m\033[3m"
RESET = "\033[0m"

# Define the beginning of the sentence
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

# Prompt the user for input
adjective = input("Please type an adjective and press enter: ")  # e.g., *tiny*
noun = input("Please type a noun and press enter: ")            # e.g., *plant*
verb = input("Please type a verb and press enter: ")            # e.g., *fly*

# Construct the final sentence
final_sentence = f"{SENTENCE_START} {BOLD_ITALIC}{adjective}{RESET} {BOLD_ITALIC}{noun}{RESET} {BOLD_ITALIC}{verb}{RESET}!"

# Print the final sentence
print(final_sentence)