def main():
    # Loop through numbers from 10 to 19 (inclusive)
    for i in range(10, 20):
        if is_odd(i):
            print(f"{i} odd")  # Print the number and "odd"
        else:
            print(f"{i} even")  # Print the number and "even"

def is_odd(value: int) -> bool:
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1  # Return True if odd, False if even

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function