def in_range(n: int, low: int, high: int) -> bool:
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True  # Return True if n is within the range

    return False  # Return False if n is outside the range

def main():
    # Example usage of the in_range function
    n = int(input("Enter a number: "))  # Prompt user for a number
    low = int(input("Enter the lower bound: "))  # Prompt user for the lower bound
    high = int(input("Enter the upper bound: "))  # Prompt user for the upper bound
    
    # Check if the number is in range and print the result
    if in_range(n, low, high):
        print(f"{n} is in the range [{low}, {high}].")
    else:
        print(f"{n} is not in the range [{low}, {high}].")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function