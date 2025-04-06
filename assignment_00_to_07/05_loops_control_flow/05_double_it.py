def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))  # Get user input and convert it to an integer
    
    # Loop until curr_value is 100 or greater
    while curr_value < 100:
        curr_value *= 2  # Double the current value
        print(curr_value)  # Print the doubled value

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function