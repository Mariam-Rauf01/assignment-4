def main():
    # Countdown from 10 to 1
    for i in range(10, 0, -1):  # Start at 10, end at 1, decrement by 1
        print(i, end=' ')  # Print the current number followed by a space
    
    print("Liftoff!")  # Print Liftoff! after the countdown

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()  # Execute the main function