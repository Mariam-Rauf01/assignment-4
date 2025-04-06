def print_ones_digit(num: int):
    """
    Prints the ones digit of the given number.
    """
    print("The ones digit is", num % 10)  # Calculate and print the ones digit

def main():
    num = int(input("Enter a number: "))  # Prompt the user for a number
    print_ones_digit(num)  # Call the function to print the ones digit

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function