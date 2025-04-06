import random  # Import the random module to generate random numbers

# Set the likelihood of the done() function returning True
DONE_LIKELIHOOD = 0.3  # Adjust this value as needed (0 to 1)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():  # Check if we should stop counting
            return  # End the function execution
        print(curr_num)  # Print the current number

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Call the chaotic counting function
    print("I'm done")  # Print when counting is finished

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == "__main__":
    main()  # Execute the main function