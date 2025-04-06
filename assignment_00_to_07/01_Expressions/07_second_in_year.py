def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far: int = 0  # Initialize the total sum to zero
    for number in numbers:  # Iterate through each number in the list
        total_so_far += number  # Add the current number to the total sum

    return total_so_far  # Return the total sum

# There is no need to edit code beyond this point

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Create a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Calculate the sum of the list
    print(sum_of_numbers)  # Print out the sum

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()