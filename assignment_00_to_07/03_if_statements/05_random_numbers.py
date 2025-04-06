import random  # Import the random module

N_NUMBERS: int = 10  # Number of random numbers to generate
MIN_VALUE: int = 1   # Minimum value for the random numbers
MAX_VALUE: int = 100 # Maximum value for the random numbers

def main():
    # Generate and print 10 random numbers in the specified range
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    print(" ".join(map(str, random_numbers)))  # Print the numbers separated by spaces

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function