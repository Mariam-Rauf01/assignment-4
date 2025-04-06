def average(a: float, b: float) -> float:
    """
    Returns the number which is halfway between a and b.
    """
    total = a + b  # Calculate the sum of a and b
    return total / 2  # Return the average

def main():
    # Calculate averages using the average function
    avg_1 = average(0, 10)  # Average of 0 and 10
    avg_2 = average(8, 10)   # Average of 8 and 10
    
    # Calculate the final average of the two averages
    final = average(avg_1, avg_2)
    
    # Print the results
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function