def double(num: int) -> int:
    """
    Returns the result of multiplying num by 2.
    """
    return num * 2  # Multiply the input number by 2 and return the result

# There is no need to edit code beyond this point

def main():
    num = int(input("Enter a number: "))  # Prompt the user for a number and convert it to an integer
    num_times_2 = double(num)  # Call the double function with the user's number
    print("Double that is", num_times_2)  # Print the result

if __name__ == '__main__':
    main()  # Execute the main function