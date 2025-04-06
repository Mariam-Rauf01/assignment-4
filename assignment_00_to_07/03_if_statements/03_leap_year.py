def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    # Check if the year is a leap year
    if year % 4 == 0:  # The year must be divisible by 4
        if year % 100 == 0:  # If it is divisible by 100
            if year % 400 == 0:  # If it is also divisible by 400
                print("That's a leap year!")  # It is a leap year
            else:  # Not divisible by 400
                print("That's not a leap year.")  # It is not a leap year
        else:  # Not divisible by 100
            print("That's a leap year!")  # It is a leap year
    else:  # Not divisible by 4
        print("That's not a leap year.")  # It is not a leap year

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function