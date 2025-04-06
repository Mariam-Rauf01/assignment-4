MAX_TERM_VALUE: int = 10000  # Constant for the maximum term value

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    
    # Loop to generate Fibonacci numbers until the current term exceeds the maximum value
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=' ')  # Print the current term followed by a space
        term_after_next = curr_term + next_term  # Calculate the next term in the sequence
        curr_term = next_term  # Move to the next term
        next_term = term_after_next  # Update the next term

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function