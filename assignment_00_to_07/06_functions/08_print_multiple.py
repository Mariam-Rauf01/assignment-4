def print_multiple(message: str, repeats: int):
    """
    Prints the message a specified number of times.
    """
    for i in range(repeats):  # Loop for the number of repeats
        print(message)  # Print the message

def main():
    message = input("Please type a message: ")  # Prompt the user for a message
    repeats = int(input("Enter a number of times to repeat your message: "))  # Prompt for the number of repeats
    print_multiple(message, repeats)  # Call the function to print the message

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function