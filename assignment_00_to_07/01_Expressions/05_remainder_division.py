# Main program
while True:
    try:
        # Prompt the user for the first number
        dividend_input = input("Please enter an integer to be divided (or type 'exit' to quit): ")
        
        # Allow the user to exit the loop
        if dividend_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        # Prompt the user for the second number
        divisor_input = input("Please enter an integer to divide by: ")
        
        # Convert inputs to integers
        dividend = int(dividend_input)
        divisor = int(divisor_input)
        
        # Perform the division and calculate the remainder
        result = dividend // divisor  # Integer division
        remainder = dividend % divisor  # Remainder
        
        # Output the result
        print(f"The result of this division is {result} with a remainder of {remainder}\n")
    
    except ValueError:
        print("Please enter valid integers.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero divisor.")